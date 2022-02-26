from flask import Flask, Response, request
from service import app,db
from service.models.models import *
from sqlalchemy import exc
from service.functions.convert import convert
@app.route("/api/veg-list", methods=["GET"])
def get_veg_list():
    try:
        veg_list = [convert(item) for item in Vegetables.query.all()]
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        print({"result": str(e.orig) + " for parameters" + str(e.params)})
        return "error", 409
    print("veg-list: ", veg_list)
    return {"list": veg_list}

@app.route("/api/orders", methods=["GET"])
def get_orders():
    try:
        order_list = [convert(order) for order in Orders.query.all()]
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        print({"result": str(e.orig) + " for parameters" + str(e.params)})
        return "error", 409
    print(order_list)
    return {"result": "successful", "orders": order_list}, 200

@app.route("/api/orders/<order_id>", methods=["GET"])
def get_orders_by_id(order_id):
    try:
        order = convert(Orders.query.filter_by(id=order_id).first())
        order_list = [convert(item) for item in Order_items.query.filter_by(order_id=order["id"]).all()]   
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        print({"result": str(e.orig) + " for parameters" + str(e.params)})
        return "error", 409
    print(order_list)
    return {"result": "successful", "order": {
        "timestamp": order["timestamp"],
        "id": order["id"],
        "list":order_list}}, 200

    