import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # MD5 hash of 'you-will-never-guess' Isto tem que ser apagado...
    SECRET_KEY = os.environ.get('SECRET_KEY') or '72760D71E01947DC8419AD9861805A37'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
