from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
SQLALCHEMY_TRACK_MODIFICATIONS = False
application.config.from_object('config')
db = SQLAlchemy(application)
