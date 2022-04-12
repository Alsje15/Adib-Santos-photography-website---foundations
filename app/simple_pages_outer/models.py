from enum import unique
from app.extensions.database import db # -> imports the ORM 


class Foto(db.Model): 
    id = db.Column(db.String(80), primary_key = True)
    slug = db.Column(db.String(80), unique = True)
    price = db.Column(db.Numeric(10, 2))
    picture_url = db.Column(db.String(80), unique = True)
    genre = db.Column(db.String(80))
    country = db.Column(db.String(80))
    city = db.Column(db.String(80))
    desctiption = db.Column(db.String(1000))
    foto_orders = db.relationship('FotoOrder', backref='order', lazy=True)



    