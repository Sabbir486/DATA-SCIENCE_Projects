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


flavor = st.selectbox("Select a flavor for your tea:", ["Lemon", "Mint", "Ginger"])

if flavor == "Lemon":
    st.write("You have selected Lemon flavor for your tea.")
elif flavor == "Mint":
    st.write("You have selected Mint flavor for your tea.")
elif flavor == "Ginger":
    st.write("You have selected Ginger flavor for your tea.")


sugar = st.slider("Select the amount of sugar you want in your tea (in teaspoons):", 0, 5, 1)

if sugar == 0:
    st.write("You have selected no sugar for your tea.")
elif sugar == 1:
    st.write("You have selected 1 teas poon of sugar for your tea.")
elif sugar == 2:
    st.write("You have selected 2 tea spoons of sugar for your tea.")
elif sugar == 3:
    st.write("You have selected 3 tea spoons of sugar for your tea.")
elif sugar == 4:
    st.write("You have selected 4 tea spoons of sugar for your tea.")
elif sugar == 5:
    st.write("You have selected 5 tea spoons of sugar for your tea.")


