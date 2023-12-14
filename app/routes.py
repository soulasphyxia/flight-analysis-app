# -*- coding: utf-8 -*-
from app import app
from flask import render_template,request
import streamlit as st
from app import db
from app import analysis
from models import Flights

@app.route("/api/data",methods=['GET'])
def index():
    current = str(request.args.get("current"))
    target = str(request.args.get("target"))
    print(current, target)
    
    flight = db.session.query(Flights).filter_by(departure_city = current,destination_city = target).first()
    print(type(flight))
    return {
        "departure_city": flight.departure_city,
        "destination_city": flight.destination_city,
        "price": flight.price
    }


