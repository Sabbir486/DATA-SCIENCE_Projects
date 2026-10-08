import streamlit as st

st.title('Make a Calculator app for counting the age')

today_date = st.date_input("Enter today's date:")
birth_date = st.date_input("Enter your date of birth:")
if today_date >= birth_date:
    age = today_date.year - birth_date.year
    st.write(f"Your age is: {age}")

else:
    st.error("Today's date cannot be earlier than your date of birth. Please enter valid dates.")