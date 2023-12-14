import streamlit as st
import numpy as np
import pandas as pd
import time
import datetime


def main():

    st.markdown("# СЕРЕГА ПОЛЕТЕЛИ 🎈")

    col1, col2, col3 = st.columns(3, gap="small")

    with col1:
        dep_city = st.selectbox(
        'Укажите свой город отправления',
        ('Томск', 'Новосибирск'))

        st.write('Город отправления:', dep_city)

    with col2:
        dest_city = st.selectbox(
            "Укажите город назначения:",
            ("Санкт-Петербург", "Москва", "Хабаровск", 
            "Иркутск", "Благовещенск", "Нерюнгри", "Мирный",
            "Южно-Сахалинск", "Петропавловск-Камчатский")
        )
        st.write('Город отправления:', dest_city)

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


    st.button("НАЖМИ МЕНЯ")

    a = [1, 2, 3, 4]
    st.write(*a)

    x = st.slider('x')  # 👈 this is a widget
    st.write(x, 'squared is', x)

    if x <= 1:
        chart_data = pd.DataFrame(
            np.random.randn(20, 4),
            columns=['a', 'b', 'c', 'd'])
    else:
        chart_data = pd.DataFrame(
            np.random.randn(x, 4),
            columns=['a', 'b', 'c', 'd'])

    st.line_chart(chart_data)

    st.sidebar.markdown("# Main page 🎈")

def counter():
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)


if __name__ == "__main__":
    main()
    counter()