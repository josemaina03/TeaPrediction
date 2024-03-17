import streamlit as st
import requests
from streamlit_extras.switch_page_button import switch_page


# Login Function
def login(username, password):
    url = "https://dsaichack.onrender.com/auth/login/"
    data = {'username': username, 'password': password}
    return requests.post(url, json=data)




BASE_URL = "https://dsaichack.onrender.com/auth/password/"

def password_reset(email):
    url = BASE_URL + "reset/"
    data = {'email': email}
    response = requests.post(url, json=data)
    return response

def password_reset_confirm(uid, token, new_password, re_new_password):
    url = BASE_URL + "reset/confirm/"
    data = {'uid': uid, 'token': token, 'new_password': new_password, 're_new_password': re_new_password}
    response = requests.post(url, json=data)
    return response
def login_page():
    if st.session_state['key'] is not None:
        switch_page("tea_price")
        
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username and password:
            response_data = login(username, password)
            if 'key' in response_data.content.decode():
                st.success(f"Welcome back, {username}!")
                st.session_state['key'] = response_data.content.decode().split('"')[3]
                switch_page("tea price")
            else:
                st.error(f"Login failed: {response_data}")
    # if st.button("Forgot Password"):
    #     entered_email = st.text_input("Enter the email you used to register")
    #     st.write(entered_email)
    # # Check if the entered email matches the one in the session state
    # if entered_email == st.session_state.get('email', ''):
    #     st.write(password_reset(entered_email).text)
        
    #     # Display the form fields only if the email check is successful
    #     uid = st.text_input("Enter the UID you received in your email")
    #     token = st.text_input("Enter the token you received in your email")
    #     new_password = st.text_input("Enter your new password", type="password")
    #     re_new_password = st.text_input("Re-enter your new password", type="password")

    #     if st.button("Reset Password"):
    #         if new_password == re_new_password:
    #             response = password_reset_confirm(uid, token, new_password, re_new_password)
    #             st.write(response.text)
                
    #             if response.status_code == 200:  # Assuming 200 is a success status code
    #                 switch_page("login")
    #             else:
    #                 st.error("Password reset failed. Please try again.")
    #         else:
    #             st.error("Passwords do not match")
    #     else:
    #         st.error("Please enter your new password")
    # else:
    #     st.error("Email does not match the one in the session state. Please try again.")

if __name__ == "__main__":
    login_page()