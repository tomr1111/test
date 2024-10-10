from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Volunteer(db.Model):
    __tablename__ = 'volunteers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)
    region = db.Column(db.String(100), nullable=False)
    roles = db.relationship('Role', secondary='volunteer_roles')

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), nullable=False)

class VolunteerRoles(db.Model):
    __tablename__ = 'volunteer_roles'
    id = db.Column(db.Integer, primary_key=True)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteers.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
