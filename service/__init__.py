from flask import Flask
from flask_cors import CORS
from os import getenv
from flask_sqlalchemy import SQLAlchemy

# create flask App
app = Flask(__name__)




# DB config - postgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DB_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = getenv("SECRET_STRING")
cors = CORS(app, resources={r"/*": {"origins": "*"}})
db = SQLAlchemy(app)

from service.routes import get_routes
from service.routes import create_tables
from service.routes import login_route
from service.routes import post_list_route

