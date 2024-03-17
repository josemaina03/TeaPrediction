import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from PIL import Image
from pages import login
#from pages import tea_price
import numpy as np


# Web app
st.title('Tea Price Prediction Model')
img = Image.open(r'C:/Users/USER/OneDrive/Desktop/Tea-Price-Prediction-Model-main/tea.jpg')
st.image(img, width=200, use_column_width=True)





# Tea Price Prediction Page
st.markdown("# Welcome to Tea Price Prediction")
st.image(r"C:\Users\USER\OneDrive\Desktop\Tea-Price-Prediction-Model-main\tea.jpg")







st.session_state['email'] = None
st.session_state['key'] = None


def main():
#
    if st.session_state['email'] is None:
        #create.signin_page()
   # elif st.session_state['key'] is None:
        login.login_page()
    else:
        st.write("Hello World")
        login.main()
    # st.write("Hello World")


if __name__ == "__main__":
    main()
