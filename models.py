from app import db

class Flights(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    departure_city = db.Column(db.String(120), index=True)
    destination_city = db.Column(db.String(120), index=True)
    date = db.Column(db.Date, index=True)
    airport = db.Column(db.String(120), index=True)
    price = db.Column(db.Float,index=True)
    data_source = db.Column(db.String(256), index=True)
    def __repr__(self):
        return f'<Flight {self.departure_city} - {self.destination_city} Price: {self.price} >'
    
class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city_name = db.Column(db.String(120), index=True)
    country = db.Column(db.String(120), index=True)
    airport_code = db.Column(db.String(120), index=True)