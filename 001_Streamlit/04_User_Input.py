import streamlit as st

st.title("About User Input")

scups = st.number_input("Enter a number:", min_value=0, max_value=100, step=2)
st.write(f"You entered: {scups}")


text = st.text_input("Enter some text:")
if text:
    st.write(f"Welcome {text} !")


dob = st.date_input("Select your date of birth:")
if dob:
    st.write(f"Your have birth on {dob}")