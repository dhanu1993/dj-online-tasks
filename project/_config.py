# project/_config.py


import os


# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
CSRF_ENABLED = True
SECRET_KEY = 'w\xfb\x80,\x8e\xf7\x92\xe6\xdb\x89\xed\x91[\xf2\xd8s\xd9V\xcc\xe2^\xb1\xa1\xd0'
DEBUG = False

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
