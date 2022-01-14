from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite//simulator_database.db'
db = SQLAlchemy(app)

from app.controllers import default