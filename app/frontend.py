import streamlit as st 
import requests


def main():
    st.title('Streamlit Frontend for Flask API')
    st.button(label ="click on me",on_click = button_on_click())



def button_on_click():
    response = requests.get('http://localhost:5000/api/data')
    data = response.json()
    
    st.write(f"Random number\n: {data['data']}")
    


if __name__ == '__main__':
    main()
    
    
