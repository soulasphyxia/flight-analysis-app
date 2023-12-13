from app import app
from flask import render_template
import streamlit as st
from app import analysis

@app.route("/api/data")
def index():
    data = analysis.get_num()
    return {'data': data}


