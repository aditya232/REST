from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Update(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer,nullable=False)
    availability = db.Column(db.Integer,nullable=False)
    date = db.Column(db.Date,nullable=False)
    room_type = db.Column(db.Boolean,nullable=False)

    def __init__(self,price,availability,date,room_type):
    	self.price = price
    	self.availability = availability
    	self.date = date
    	self.room_type = room_type
