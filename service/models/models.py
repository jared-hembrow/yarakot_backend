from service import db

class Vegetables(db.Model):
    id = db.Column(db.String, primary_key=True)
    englishName = db.Column(db.String, nullable=False)
    hebrewName = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)


    def __repr__(self):
        return f"Organization(id: {self.id} Name: {self.englishName})"
    
    def __init__(self, id, englishName, hebrewName, url):
        self.id = id
        self.englishName = englishName
        self.hebrewName = hebrewName
        self.url = url

class Orders(db.Model):
    id = db.Column(db.String, primary_key=True)
    list = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f"Organization(id: {self.id} Name: {self.timestamp})"
    
    def __init__(self, id, list, timestamp):
        self.id = id
        self.list = list
        self.timestamp = timestamp

class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    Name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)


    def __repr__(self):
        return f"Organization(id: {self.id} Name: {self.name})"
    
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password
