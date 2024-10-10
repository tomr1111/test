from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volunteer.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # 用于闪现消息
db = SQLAlchemy(app)

# 志愿者模型
class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    region = db.Column(db.String(100), nullable=False)
    roles = db.Column(db.String(200), nullable=False)

# 首页
@app.route('/')
def index():
    volunteers = Volunteer.query.all()
    return render_template('index.html', volunteers=volunteers)

# 添加志愿者
@app.route('/add', methods=['GET', 'POST'])
def add_volunteer():
    if request.method == 'POST':
        name = request.form['name']
        region = request.form['region']
        roles = request.form['roles']
        new_volunteer = Volunteer(name=name, region=region, roles=roles)
        db.session.add(new_volunteer)
        db.session.commit()
        flash('Volunteer added successfully!')
        return redirect(url_for('index'))
    return render_template('add_volunteer.html')

# 编辑志愿者
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_volunteer(id):
    volunteer = Volunteer.query.get_or_404(id)
    if request.method == 'POST':
        volunteer.name = request.form['name']
        volunteer.region = request.form['region']
        volunteer.roles = request.form['roles']
        db.session.commit()
        flash('Volunteer updated successfully!')
        return redirect(url_for('index'))
    return render_template('edit_volunteer.html', volunteer=volunteer)

# 删除志愿者
@app.route('/delete/<int:id>')
def delete_volunteer(id):
    volunteer = Volunteer.query.get_or_404(id)
    db.session.delete(volunteer)
    db.session.commit()
    flash('Volunteer deleted successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


