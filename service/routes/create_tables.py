from flask import Flask, Response, request
from service import app,db
from service.models.models import *
from sqlalchemy import exc

# creates all tables in the service/models folders in the DB connected to DB (var)
@app.route('/create-all', methods=['GET'])
def create_all_tables():
    db.create_all()
    return Response("done", 200)

@app.route("/push-data", methods=["GET"])
def push_data():
    db.drop_all()
    db.create_all()
    user = User(name="user", password="12345")
    db.session.add(user)
    for item in defaultList:
      add = Vegetables(englishName=item["englishName"], hebrewName=item["hebrewName"], url=item["url"])
      db.session.add(add)
    try:
        db.session.commit()
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        print({"result": str(e.orig) + " for parameters" + str(e.params)})
        return "error", 409
    return Response("done", 200)

defaultList = [
  {
    "englishName": "tomato",
    "hebrewName": "עגבנייה",
    "url": "https://i.imgur.com/vKv4Ki1.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 1,
  },
  {
    "englishName": "roma tomato",
    "hebrewName": "עגבנייה תמר",
    "url": "https://i.imgur.com/5BKJ10k.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "cherry tomato",
    "hebrewName": "עגבניית שרי",
    "url": "https://i.imgur.com/Vi73cxz.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 2,
  },
  {
    "englishName": "chocolate cherry tomato",
    "hebrewName": "עגבניות שרי שוקולד",
    "url": "https://i.imgur.com/h6Zrb6g.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "cucumber",
    "hebrewName": "מלפפון",
    "url": "https://i.imgur.com/lUZUwS1.png",
    "amount": 0,
    "containerType": "box",
    "order": 3,
  },
  {
    "englishName": "red pepper",
    "hebrewName": "פלפל אדום",
    "url": "https://i.imgur.com/RWAwsaQ.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 4,
  },
  {
    "englishName": "green pepper",
    "hebrewName": "פלפל ירוק",
    "url": "https://i.imgur.com/7snOPv1.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 5,
  },
  {
    "englishName": "orange pepper",
    "hebrewName": "פלפל כתום",
    "url": "https://i.imgur.com/iZ4mFH9.png",
    "amount": 0,
    "containerType": "box",
    "order": 6,
  },
  {
    "englishName": "yellow pepper",
    "hebrewName": "פלפל צהוב",
    "url": "https://i.imgur.com/KgXaJOq.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 7,
  },
  {
    "englishName": "hot pepper",
    "hebrewName": "פלפל חריף",
    "url": "https://i.imgur.com/xKZjX3F.png",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "chilli pepper",
    "hebrewName": "פלפל צ'ילי",
    "url": "https://i.imgur.com/QscYDAs.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "pear",
    "hebrewName": "אגס",
    "url": "https://i.imgur.com/EYvPZ7z.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "kewi",
    "hebrewName": "קיווי",
    "url": "https://i.imgur.com/RbAl6Dc.png",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "persimmon",
    "hebrewName": "אֲפַרסְמוֹן",
    "url": "https://i.imgur.com/IQrC4XW.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "nectarine",
    "hebrewName": "נקטרינה",
    "url": "https://i.imgur.com/pHxCVOg.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "peach",
    "hebrewName": "אפרסק",
    "url": "https://i.imgur.com/1ie0M6I.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "plum",
    "hebrewName": "שזיף",
    "url": "https://i.imgur.com/CpHBlFc.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "passionfruit",
    "hebrewName": "פסיפלורה",
    "url": "https://i.imgur.com/RkUghoM.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "guava",
    "hebrewName": "גויאבה",
    "url": "https://i.imgur.com/XJYQCVA.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "pink lady apple",
    "hebrewName": "תפוח ליידי ורוד",
    "url": "https://i.imgur.com/ZAzvSHZ.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "grand apple",
    "hebrewName": "תפוח גדול",
    "url": "https://i.imgur.com/yTXzouh.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "gold apple",
    "hebrewName": "תפוח זהב",
    "url": "https://i.imgur.com/7gwIaGX.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "red apple",
    "hebrewName": "תפוח אדום",
    "url": "https://i.imgur.com/L4ZqmGQ.png",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },

  {
    "englishName": "white cabbage",
    "hebrewName": "כרוב לבן",
    "url": "https://i.imgur.com/sXkMJyM.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "red cabbage",
    "hebrewName": "כרוב אדום",
    "url": "https://i.imgur.com/sTmJsaC.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "squash",
    "hebrewName": "קישוא",
    "url": "https://i.imgur.com/bEDnMZo.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "zucchini",
    "hebrewName": "זוקיני",
    "url": "https://i.imgur.com/cXcuykv.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "eggplant",
    "hebrewName": "חציל",
    "url": "https://i.imgur.com/QSzi5Pk.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "clementina",
    "hebrewName": "קלמנטינה",
    "url": "https://i.imgur.com/XWxisyO.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
  {
    "englishName": "orange",
    "hebrewName": "תפוז",
    "url": "https://i.imgur.com/KISKPew.jpg",
    "amount": 0,
    "containerType": "box",
    "order": 0,
  },
]