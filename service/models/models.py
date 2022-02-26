from service import db

class Vegetables(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    englishName = db.Column(db.String, nullable=False)
    hebrewName = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)


    def __repr__(self):
        return f"Organization(Name: {self.englishName})"
    
    def __init__(self, englishName, hebrewName, url):
        self.englishName = englishName
        self.hebrewName = hebrewName
        self.url = url

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.BigInteger, nullable=False)
    order_items = db.relationship('Order_items', backref='order items', lazy=True)



    def __repr__(self):
        return f"Organization(Name: {self.timestamp})"
    
    def __init__(self, timestamp):
        self.timestamp = timestamp

class Order_items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    englishName = db.Column(db.String, nullable=False)
    hebrewName = db.Column(db.String, nullable=False)
    amount = db.Column(db.String, nullable=False)
    containerType = db.Column(db.String, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))


    def __repr__(self):
        return f"Organization(Name: {self.englishName}, order_id: {self.order_id})"
    
    def __init__(self, englishName, hebrewName, amount, containerType, order_id):
        self.englishName = englishName
        self.hebrewName = hebrewName
        self.amount = amount
        self.containerType = containerType
        self.order_id = order_id

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)


    def __repr__(self):
        return f"Organization(Name: {self.name})"
    
    def __init__(self, name, password):
        
        self.name = name
        self.password = password
