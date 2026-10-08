import streamlit as st

st.title("About Favourite Programming Language")

st.text('Choose your favourite programming language from the options below!')
selectbox = st.selectbox("Select your favourite programming language: ", ["Python", "JavaScript", "Java", "C++", "Ruby"])
st.write(f'Thanks for selecting {selectbox} as your favourite programming language!')

st.success("Thank you for selecting your favourite programming language!")
