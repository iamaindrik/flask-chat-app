import streamlit as st
import requests

# Simple Streamlit app for demo
st.title('Chat Application Interface')

# Input for user credentials
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Buttons for actions
if st.button('Login'):
    st.write(f'Logging in as {username}')
    # Example interaction with your Flask backend (adjust URL and logic)
    # response = requests.post('http://localhost:5000/login', data={'username': username, 'password': password})
    # st.write(response.json())

if st.button('Register'):
    st.write(f'Registering {username}')
    # Example interaction with your Flask backend
    # response = requests.post('http://localhost:5000/register', data={'username': username, 'password': password})
    # st.write(response.json())
