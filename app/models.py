# from app import db

# class Flights(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     departure_city = db.Column(db.String(120), index=True)
#     destination_city = db.Column(db.String(120), index=True)
#     date = db.Column(db.Date, index=True)
#     cost = db.Column(db.Integer, index=True)
#     airport = db.Column(db.String(120), index=True)
#     price = db.Column(db.Real,index=True)
#     data_source = db.Column(db.String(256), index=True)
    
# class Cities(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     city_name = db.Column(db.String(120), index=True)
#     country = db.Column(db.String(120), index=True)
#     airport_code = db.Column(db.String(120), index=True)