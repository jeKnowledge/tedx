from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Orator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    job = db.Column(db.String(120))
    age = db.Column(db.String(3))
    info = db.Column(db.String(127))
    photo = db.Column(db.String(255))

    def __init__(self, name, job, age, info):
        self.name = name
        self.job = job
        self.age = age
        self.info = info

    def set_photo(self, photo):
        self.photo = photo

    def __repr__(self):
        return '<User {}>'.format(self.name)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
