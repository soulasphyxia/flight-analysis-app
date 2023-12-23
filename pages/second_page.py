import streamlit as st
import numpy as np
import pandas as pd
import time
import datetime
import json
import requests
import openpyxl
import excel_parser as parser


def main():
    uploaded_file = st.file_uploader("Загрузите файл с данными о командировке в формате .xlxs:")
    if uploaded_file is not None:
        data = parser.parse(uploaded_file)   
        if st.button("Спрогнозировать"):
            st.write(data)

if __name__ == "__main__":
    main()
