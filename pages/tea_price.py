import streamlit as st
import smtplib
from email.mime.text import MIMEText
import requests
from streamlit_extras.switch_page_button import switch_page

# logout
def logout():
    url = "https://dsaichack.onrender.com/auth/logout/"
    data = {'key': st.session_state['key']}
    return requests.post(url, json=data)

# input form for tea price prediction and bonus calculation
def input_form():
    with st.form("tea_price_form"):
        st.markdown("### Tea Price Prediction and Bonus Calculation")
        st.write("Provide information for tea price prediction and bonus calculation")

        st.write("Enter Tea Types:")
        black_quantity = st.number_input("Black Tea Quantity (kg)", min_value=0.1, value=1.0, step=0.1)
        oolong_quantity = st.number_input("Oolong Tea Quantity (kg)", min_value=0.1, value=1.0, step=0.1)
        white_quantity = st.number_input("White Tea Quantity (kg)", min_value=0.1, value=1.0, step=0.1)
        green_quantity = st.number_input("Green Tea Quantity (kg)", min_value=0.1, value=1.0, step=0.1)

        submit = st.form_submit_button("Submit")

    if submit:
        st.session_state['black_quantity'] = black_quantity
        st.session_state['oolong_quantity'] = oolong_quantity
        st.session_state['white_quantity'] = white_quantity
        st.session_state['green_quantity'] = green_quantity
        st.session_state['email'] = st.text_input("Enter your email")  # Initialize the email key

        return black_quantity, oolong_quantity, white_quantity, green_quantity

# function to predict tea price based on a simple calculation
def predict_tea_price(black_quantity, oolong_quantity, white_quantity, green_quantity):
    # Placeholder logic for predicting tea prices based on input quantities
    # You can replace this with your actual logic for predicting tea prices
    # This is just a placeholder
    tea_price_prediction = black_quantity * 2 + oolong_quantity * 3 + white_quantity * 4 + green_quantity * 5

    return tea_price_prediction

# function to calculate bonus based on tea price
def calculate_bonus(tea_price):
    # Assuming a simple bonus calculation logic
    # You can replace this with your actual bonus calculation logic
    bonus_percentage = 5  # Adjust this based on your business rules
    bonus_amount = (bonus_percentage / 100) * tea_price

    return bonus_amount

# function to send email
def send_email(tea_price_prediction, bonus_amount):
    email_sender = 'josephmuhia257@gmail.com'  # Replace with your email
    email_receiver = st.session_state['email']
    subject = 'Tea Price Prediction and Bonus Calculation'
    body = f"Your predicted tea price is ${tea_price_prediction:.2f} " \
           f"and your bonus amount is ${bonus_amount:.2f}.\n\nRegards,\n\nTea Price Prediction Team"
    password = 'your_email_password'  # Replace with your email password

    try:
        msg = MIMEText(body)
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg['Subject'] = subject

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_sender, password)
        server.sendmail(email_sender, email_receiver, msg.as_string())
        server.quit()

        st.success('Email sent successfully! 🚀')
    except Exception as e:
        st.error(f"Error sending email: {e}")

# main function for the Streamlit app
def main():
    st.write("Welcome to the Tea Price Prediction and Bonus Calculation App")
    st.write("Please fill in the details below to predict tea price and calculate bonus.")
    
    user_input = input_form()

    if user_input is not None:
        black_quantity, oolong_quantity, white_quantity, green_quantity = user_input

        tea_price_prediction = predict_tea_price(black_quantity, oolong_quantity, white_quantity, green_quantity)
        bonus_amount = calculate_bonus(tea_price_prediction)

        st.success("Prediction and bonus calculation completed successfully!")
        st.write(f"Predicted Tea Price: Ksh{tea_price_prediction:.2f}")
        st.write(f"Bonus Amount: Ksh{bonus_amount:.2f}")

        send_email(tea_price_prediction, bonus_amount)

    if st.button("Logout"):
        if logout().status_code == 200:
            st.session_state['key'] = None
            switch_page("login")

if __name__ == "__main__":
    main()
