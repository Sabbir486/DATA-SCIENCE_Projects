import streamlit as st

st.title("Streamlit Basics - This is a title")
st.subheader("This is a subheader")

st.text('Welcome your first Streamlit app!')
st.write("This is a write command, which can be used to display text, data, and more.")

selectbox = st.selectbox("Choose an option: ", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {selectbox}")

st.success("This is a success message!")