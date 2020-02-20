from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
import connexion

app = connexion.FlaskApp(__name__)

application = app.app

application.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application)
ma = Marshmallow(application)