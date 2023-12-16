import streamlit as st
import numpy as np
import pandas as pd
import time
import datetime
import json
import requests

#Configure page
st.set_page_config(
        page_title="Прогнозирование цен на авиабилеты",
        page_icon="🛫",
        layout="wide"
    )

def main():
    '''Здесь задается конфигурация страницы, необходимые поля, 
    небольшая логика, которая обеспечивает, чтобы переданные данные о
    времени вылета и прилета будут адекватны, то есть не получится такого,
    что сотрудник выберит дату прилета, который будет проходить раньше вылета.'''

    st.markdown("# Прогнозирование цен на авиабилеты 🛫")

    # Поля, для ввода информации будут распределяться по трем колонкам, 
    # с небольшим интервалом между друг другом
    col1, col2, col3 = st.columns(3, gap="small")
    # Первая колонка, в которой выбирается город вылета
    with col1:
        dep_city = st.selectbox(
        'Укажите свой город отправления',
        ('Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'))

        st.write('Город отправления:', dep_city)
    # Вторая колонка, в которой выбирается город назначения
    with col2:
        dest_city = st.selectbox(
            "Укажите город назначения:",
            ('New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad')
        )
        st.write('Город отправления:', dest_city)


    # Контейнер для вывода вариантов полета
    cont = st.container()
    
    # Выпадающие меню для выбора городов прибытия и отправления
    with col3:
        
        sub_col1, sub_col2 = st.columns(2, gap="small")
        
        with sub_col1:
            departure_d = st.date_input("Дата вылета:", value=None, format="YYYY.MM.DD")
            date = departure_d
            if st.button("Найти"):
                button_click(dep_city, dest_city, date, cont)
        
def create_div(index, note, date):
    # Разные

    
    with st.form(f"Окно с билетом: {index}"):
        
        col1, col2 = st.columns(2, gap="small")
        
        with col1:

            sub_col1, sub_col2 = st.columns(2, gap="medium")

            with sub_col1:
                price = note['price'] * 1.08
                st.write(f"Цена: {round(price,2)} ₽")
                #Разные
                if st.form_submit_button(f"Купить билет: {index}"):
                    buy_ticket()
            with sub_col2:
                company = note["airline"]
                st.write(f"Авиакомпания: {company}")
        with col2:
            
            sub_col1, sub_col2 = st.columns(2, gap="medium")
            
            with sub_col1:
                st.write(f"Дата вылета: {date}")

def buy_ticket():
    st.write("Билет куплен")

def button_click(city1, city2, date, cont):
    '''Кнопка нужна для того, чтобы отправлять информацию 
    о выбранном времени вылета/прилета в базу данных.'''
   
    url = f'http://127.0.0.1:5000/api/data?dep={city1}&dest={city2}&date={date}&info=no-info'

    response = requests.get(url)
    
    data = response.json()

    with cont:
        k = 1
        for note in data['prices']:
            create_div(k, note, date)
            k += 1


if __name__ == "__main__":
    main()