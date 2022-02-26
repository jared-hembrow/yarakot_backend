from flask import Flask, Response, request
from service import app,db
from service.models.models import *
from sqlalchemy import exc
from service.functions.convert import convert
import json

@app.route("/api/insert-order", methods=["POST"])
def post_veg_order():
    # parse body of post request
    try:
        request_body = request.json
    except:
        return "error in body of request", 400
        
    print("Body of request: ", request_body)

    # check if body of request is in the right format
    if request_body is None:
        return "No body on request", 400
    if not "list" in request_body.keys():
        return "error in body of request", 400
    if not "timestamp" in request_body.keys():
        return "error in body of request", 400
    try:
        print("type: ",request_body["timestamp"])
        veg_order = Orders(timestamp=request_body["timestamp"])
        db.session.add(veg_order)
        db.session.commit()
        order_id = Orders.query.filter_by(timestamp=request_body["timestamp"]).first()
        print(veg_order.id)
        for item in request_body["list"]:
            insert_item = Order_items(
                englishName=item["englishName"],
                hebrewName=item["hebrewName"],
                amount=item["amount"],
                containerType=item["containerType"],
                order_id=order_id.id
                )
            db.session.add(insert_item)
        db.session.commit()
    except exc.SQLAlchemyError as e:
        print("problem here")
        db.session.rollback()
        print({"result": str(e.orig) + " for parameters" + str(e.params)})
        return "error", 400
    return {"result": "successful"}, 200
    