# -*- coding: utf-8 -*-
from app import app
from flask import request
from app import analysis

@app.route("/api/data",methods=['GET'])
def get_predict():
    airlines = ["IndiGo","Air India", "SpiceJet","Vistara"]
    departure = str(request.args.get("dep"))
    destination = str(request.args.get("dest"))
    departure_date = str(request.args.get("depdate"))
    back_date = str(request.args.get("backdate"))
    total_stops = 'non-stop'
    info = 'no-info'
    route = 1.0
    predict = {
        "departure city": departure,
        "destination city": destination,
        "departure_date": departure_date,
        "back_date": back_date,
        "prices":[]
    }
    sorted_prices_departure = {}
    sorted_prices_back = {}
    for airline in airlines:
        departure_price = float(analysis.get_predict(airline, departure_date, departure, destination, total_stops, info, route))
        back_price = float(analysis.get_predict(airline, back_date, destination, departure, total_stops, info, route))
        sorted_prices_departure[airline] = departure_price
        sorted_prices_back[airline] = back_price
    sorted_prices_departure = {sorted_prices_departure: v for sorted_prices_departure, v in sorted(sorted_prices_departure.items(), key=lambda item: item[1])}
    sorted_prices_back = {sorted_prices_back: v for sorted_prices_back, v in sorted(sorted_prices_back.items(), key=lambda item: item[1])}
    
    dest_airlines = list(sorted_prices_departure.keys())
    back_airlines = list(sorted_prices_back.keys())
    
    for i in range(len(dest_airlines)):
        dest_airline = dest_airlines[i]
        back_airline = back_airlines[i]
        total_cost = sorted_prices_departure[dest_airline] + sorted_prices_back[back_airline]
        price = {
            "airlines": ','.join([dest_airline,back_airline]),
            "price": total_cost * 1.08
        }
        
        predict["prices"].append(price)
        
            
    return predict

@app.route("/api/data/lowestcost",methods=['GET'])
def get_lowest_price():
    airlines = ["IndiGo","Air India", "SpiceJet","Vistara"]
    departure = str(request.args.get("dep"))
    destination = str(request.args.get("dest"))
    departure_date = str(request.args.get("depdate"))
    back_date = str(request.args.get("backdate"))
    total_stops = 'non-stop'
    info = 'no-info'
    route = 1.0
    sorted_prices_departure = {}
    sorted_prices_back = {}
    for airline in airlines:
        departure_price = float(analysis.get_predict(airline, departure_date, departure, destination, total_stops, info, route))
        back_price = float(analysis.get_predict(airline, back_date, destination, departure, total_stops, info, route))
        sorted_prices_departure[airline] = departure_price
        sorted_prices_back[airline] = back_price
    sorted_prices_departure = {sorted_prices_departure: v for sorted_prices_departure, v in sorted(sorted_prices_departure.items(), key=lambda item: item[1])}
    sorted_prices_back = {sorted_prices_back: v for sorted_prices_back, v in sorted(sorted_prices_back.items(), key=lambda item: item[1])}
    
    dest_airlines = list(sorted_prices_departure.keys())
    back_airlines = list(sorted_prices_back.keys())
    
    cheapest_dest_airline = dest_airlines[0]
    cheapest_back_airline = back_airlines[0]
    
    cheapest_price = sorted_prices_departure[cheapest_dest_airline] + sorted_prices_back[cheapest_back_airline]
    
    predict = {
        "airlines": ','.join([cheapest_dest_airline,cheapest_back_airline]),
        "price": cheapest_price
    }
        
            
    return predict


