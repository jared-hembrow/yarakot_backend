from flask import Flask
from dotenv import load_dotenv
from os import getenv
from flask_sqlalchemy import SQLAlchemy

# create flask App
app = Flask(__name__)

# env config
load_dotenv()


# DB config - postgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DB_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = getenv("SECRET_STRING")
db = SQLAlchemy(app)

from service.routes import get_routes
