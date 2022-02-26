from flask import Flask, Response, request
from service import app,db
from service.models.models import *
from sqlalchemy import exc


@app.route('/api/login', methods=["POST"])
def log_user_in():
    # parse body of post request
    try:
        request_body = request.json
    except:
        return "error in body of request", 400
        
    print("Body of request: ", request_body)

    # check if body of request is in the right format
    if request_body is None:
        return "No body on request", 400
    if not "password" in request_body.keys():
        return "error in body of request", 400
    # query DB
    check = User.query.filter_by(password=request_body["password"]).first()
    if check is None:
        return {"result": "incorrect"}, 403
    print(check)
    return {"result": "successful"}, 200