from app.extensions.database import db, CRUDMixin
from datetime import datetime

class Order(db.Model, CRUDMixin): 
  id = db.Column(db.Integer, primary_key = True)
  street = db.Column(db.String(80))
  city = db.Column(db.String(80))
  zip = db.Column(db.String(80))
  country = db.Column(db.String(80))
  foto_id = db.Column(db.Integer)
  user = db.Column(db.String(80))

class Foto(db.Model, CRUDMixin): 
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(80), unique = True)
  price = db.Column(db.Numeric(10, 2))
  picture_url = db.Column(db.String(80))
  genre = db.Column(db.String(80))
  country = db.Column(db.String(80))
  city = db.Column(db.String(80))



#   foto_id = db.Column(db.Integer, db.ForeignKey('foto.id'), nullable = False)
# let's find out how the foto_id is called 