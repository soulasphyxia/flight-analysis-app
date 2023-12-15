# -*- coding: utf-8 -*-
from app import app
from flask import request

from app import analysis
# GET:/api/data?current=&target=&date= => price
@app.route("/api/data",methods=['GET'])
def index():
    departure = str(request.args.get("dep"))
    destination = str(request.args.get("dest"))
    airline = str(request.args.get("airline"))
    date = str(request.args.get("date"))
    total_stops = 'non-stop'
    info = str(request.args.get("info"))
    route = 2.0
    

    cost = analysis.get_num(airline, date, departure, destination, total_stops, info, route)
    
    return {"data": cost}


