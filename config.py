import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secure_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///volunteer.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
