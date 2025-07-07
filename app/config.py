# This file will hold all our configuration variables. 
# This includes your SECRET_KEY, the database location (SQLALCHEMY_DATABASE_URI), and 
# any other settings. This keeps sensitive information and settings separate from 
# your application logic.

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite///' + os.path.join(basedir, 'libraryApp.db')
    SQLACLHEMY_TRACK_MODIFICATIONS = False