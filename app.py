from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 创建 Flask 应用
app = Flask(__name__)

# 配置数据库，使用 SQLite 数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volunteer.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化数据库
db = SQLAlchemy(app)

# 定义志愿者模型
class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    region = db.Column(db.String(100), nullable=False)
    roles = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Volunteer {self.name}>"

# 定义主页面路由
@app.route('/')
def index():
    return "Welcome to the Volunteer Management System"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
