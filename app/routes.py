# -*- coding: utf-8 -*-
from app import app
from flask import request
from app import analysis

@app.route("/api/data",methods=['GET'])
def get_predict():
    airlines = ["IndiGo","Air India", "SpiceJet","Vistara"]
    departure = str(request.args.get("dep"))
    destination = str(request.args.get("dest"))
    date = str(request.args.get("date"))
    total_stops = 'non-stop'
    info = 'no-info'
    route = 1.0
    predict = {
        "departure city": departure,
        "destination city": destination,
        "date": date,
        "prices":[]
    }
    sorted_prices = {}
    for airline in airlines:
        price = float(analysis.get_predict(airline, date, departure, destination, total_stops, info, route))
        sorted_prices[airline] = price
    sorted_prices = {sorted_prices: v for sorted_prices, v in sorted(sorted_prices.items(), key=lambda item: item[1])}
    for airline in sorted_prices.keys():
        airline_price = {
            "airline": airline,
            "price": sorted_prices[airline]
        }
        predict["prices"].append(airline_price)
    return predict


