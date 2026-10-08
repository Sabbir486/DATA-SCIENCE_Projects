import streamlit as st

st.title("Conditional Statements in Python")

if st.button("Make a Chai"):
    st.success("Your tea is ready! Enjoy your cup of Chai!")


checkbox = st.checkbox("Add Milk")

if checkbox:
    st.write("Adding milk to your tea.")
else:
    st.write("No milk will be added to your tea.")

tea_type = st.radio("Select the type of tea you want:", ["Green Tea", "Black Tea", "Herbal Tea"])

if tea_type == "Green Tea":
    st.write("You have selected Green Tea.")
elif tea_type == "Black Tea":
    st.write("You have selected Black Tea.")
elif tea_type == "Herbal Tea":
    st.write("You have selected Herbal Tea.")


