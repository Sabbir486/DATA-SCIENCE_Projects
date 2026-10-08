import streamlit as st
import requests

st.title("Making a Web Request!")
amount = st.number_input("Enter the amount in INR:", min_value=1, max_value=100000)

target_currency = st.selectbox("Select the currency you want to convert to:", ["USD", "EUR", "GBP", "JPY", "AUD"])

if st.button("Convert"):
    url = f"https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        conversion_rate = data["rates"][target_currency]
        converted_amount = conversion_rate * amount
        st.success(f"{amount} INR is equal to {converted_amount:.2f} {target_currency}")

    else:
        st.error("Failed to fetch exchange rates. Please try again later.")
