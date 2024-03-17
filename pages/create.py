import streamlit as st
import requests
from streamlit_extras.switch_page_button import switch_page



def signup(username, email, password):
    url = "https://dsaichack.onrender.com/register/"
    data = {'username': username, 'email': email, 'password': password}
    return requests.post(url, json=data)




def signin_page():
    if st.session_state['email'] is not None:
        switch_page("login")

    st.header("Signup")
    username = st.text_input("Username")
    email = st.text_input('Email')
    password = st.text_input("Password", type="password")

    if st.button("Signup"):
        if username and password and email:
            signup(username, email, password)
            st.session_state['username'] = username
            st.session_state['email'] = email
            st.success("User successfully registered!") 
            switch_page("login")






if __name__ == "__main__":
    signin_page()