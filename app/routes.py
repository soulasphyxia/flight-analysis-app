from app import app
from flask import render_template,request
import streamlit as st
from app import analysis

@app.route("/api/data",methods=['GET'])
def index():
    current = request.args.get("current")
    target = request.args.get("target")
    
    cost = analysis.get_num()
    return {
        "data": cost
    }


