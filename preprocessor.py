from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
import pandas as pd
import streamlit as st


# Load the data once outside the functions
DATA = "Data/loan-train.csv"
df = pd.read_csv('C:\Users\USER\OneDrive\Desktop\Tea-Price-Prediction-Model-main\tea_price_data.csv')
# st.dataframe(df.head())

df['Dependents'].astype(str)

column_names_ = ['Black','Green','Oolong','White','EUR/USD']
min_max_cols = ['EUR/USD']
Label_cols = ['Black','Green','Oolong','White','EUR/USD']

column_names =  df.columns[1:-1]
# st.write(column_names)
# Create an instance of StandardScaler
scaler = StandardScaler()
minax = MinMaxScaler()
label_encoders={}



   
num_scaler = scaler.fit(df[column_names_])
minmax_scaler = minax.fit(df[min_max_cols])
for i in Label_cols:
    encoders = LabelEncoder().fit(df[i])
    label_encoders[i] = encoders    

# st.write("label_encoders: ", label_encoders)