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
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
db = SQLAlchemy(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route("/", methods=["GET"])
def home():
    return "Home Page"


from service.routes import get_routes
from service.routes import create_tables
from service.routes import login_route
from service.routes import post_list_route

