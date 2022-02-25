from flask import Flask, request, Response
from service import app,db

from datetime import datetime

@app.route("/veg-list", methods=["GET"])
def test():
    veg_list = [convert(item) for item in db.Vegetables.query.all()]
    return {"list": veg_list}
    