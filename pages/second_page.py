import streamlit as st
import json
import requests
import excel_parser as parser


def main():
    uploaded_file = st.file_uploader("Загрузите файл с данными о командировке в формате .xlxs:")
    container = st.container()
    if uploaded_file is not None:
        data = parser.parse(uploaded_file)   
        if st.button("Спрогнозировать"):
            on_click_btn(data,container)

def on_click_btn(data, contaier):
    with contaier:
        i = 1
        for trip in data:
            departure_city = trip["departure_city"]
            destination_city = trip["destination_city"]
            departure_date = trip["departure_date"]
            back_date = trip["back_date"]
            cost_date = make_request(departure_city,departure_city, departure_date, back_date)
            trip["airlines"] = cost_date["airlines"]
            trip["price"] = cost_date["price"]
            create_trip_info(i, trip)
            i += 1

def create_trip_info(index, trip):
    with st.form(f"Командировка: {index}"):
        col1, col2, col3 = st.columns(3, gap="small")
        with col1:
            sub_col1, sub_col2 = st.columns(2, gap="small")
            with sub_col1:
                name = trip['name'] 
                st.write(f"ФИО сотрудника: {name}")
            with sub_col2:
                location = trip["departure_city"] + " - " + trip["destination_city"]
                st.write(f"Локация:\n {location}")
        with col2:
            sub_col1, sub_col2 = st.columns(2, gap="small")
            with sub_col1:
                departure_date = trip["departure_date"]
                st.write(f"Дата вылета: {departure_date}")
            with sub_col2:
                back_date = trip["back_date"]
                st.write(f"Дата вылета обратно: {back_date}")
        with col3:
            sub_col1, sub_col2 = st.columns(2, gap="small")
            with sub_col1:
                price = trip["price"]
                st.write(f"Цена {price} ₽")
            with sub_col2:
                airlines = trip["airlines"]
                st.write(f"Авиакомпании: {airlines}")
            if st.form_submit_button("Оформить билеты"):
                return
def make_request(city1, city2, departure_date, back_date):
    url = f'https://flight-analysis-app-production.up.railway.app/api/data/lowestcost?dep={city1}&dest={city2}&depdate={departure_date}&backdate={back_date}&info=no-info'
    #url = f'http://127.0.0.1:5000/api/data/lowestcost?dep={city1}&dest={city2}&depdate={departure_date}&backdate={back_date}&info=no-info'
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    main()
