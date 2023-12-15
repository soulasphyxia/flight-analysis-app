import streamlit as st
import numpy as np
import pandas as pd
import time
import datetime
import requests


def main():

    st.markdown("# СЕРЕГА ПОЛЕТЕЛИ 🎈")
    
    col1, col2, col3 = st.columns(3, gap="small")

    with col1:
        dep_city = st.selectbox(
        'Укажите свой город отправления',
        ('Banglore', 'Новосибирск'))

        st.write('Город отправления:', dep_city)

    with col2:
        dest_city = st.selectbox(
            "Укажите город назначения:",
            ('New Delhi','sfsfs')
        )
        st.write('Город отправления:', dest_city)
    if st.button("НАЖМИ МЕНЯ") : btn_on_click(dep_city, dest_city) 
    with col3:
        
        sub_col1, sub_col2 = st.columns(2, gap="small")
        
        with sub_col1:
            z1 = datetime.date.today()
            departure_d = st.date_input("Дата вылета:", z1, format="DD.MM.YYYY")
        
        with sub_col2:
            z2 = datetime.date.today()
            arrival_d = st.date_input("Дата прилета:",z2, format="DD.MM.YYYY")

            if arrival_d < departure_d:
                z2 = z1
                st.write("Все красиво")

    


#http://127.0.0.1:5000/api/data?dep=Banglore&dest=New Delhi&airline=IndiGo&date=2024-03-14&info=no-info
def btn_on_click(dep, dest):
    url = "http://127.0.0.1:5000/api/data"
    response = requests.get(url)
    data = response.json()
    print(data)
    st.write(data["data"])

if __name__ == "__main__":
    main()