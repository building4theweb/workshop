import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

# App Config
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
DATABASE_URI = 'sqlite:///{}/soundem.db'.format(BASE_PATH)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

# Flask-Security Config
app.config['SECURITY_CONFIRMABLE'] = False

# Initialize database
db = SQLAlchemy(app)

from soundem import models, views