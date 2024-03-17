from google.oauth2 import id_token
from google.auth.transport import requests
import streamlit as st
import dotenv
import os


dotenv.load_dotenv(".env")



def main():
#     st.title("Your Streamlit App")
    
#     # Google Authentication
#     st.subheader("Google Authentication")
#     client_id = os.getenv('CLIENTID')  # Replace with your OAuth client ID
#     token = os.getenv('IDTOKEN')
#     st.write(f'Client ID {client_id}  Token: {token}')
    
#     try:
#         idinfo = id_token.verify_oauth2_token(token, requests.Request(), client_id)
#         st.write(idinfo)
#         if idinfo['aud'] != client_id:
#             raise ValueError("Invalid client ID")
#         st.success(f"Authentication successful: {idinfo['name']}")
#         st.write(idinfo)
#         # Continue with the rest of your app logic here
#     except ValueError as e:
#         st.error("Authentication failed")
        
    
#         # return st.success("You've successfully Authed!")
#     # ...
    

    print('register')
if __name__ == "__main__":
    main()



    