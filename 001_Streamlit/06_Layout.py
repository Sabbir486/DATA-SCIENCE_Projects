import streamlit as st

st.title("Streamlit Layouts")
st.markdown('### Welcome to Vote')

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Vote C++")
    vote_cpp = st.button("Vote for C++")

with col2:
    st.header("Vote Python")
    vote_python = st.button("Vote for Python")

with col3:
    st.header("Vote Java")
    vote_java = st.button("Vote for Java")

if vote_cpp:
    st.success("You voted for C++!")

elif vote_python:
    st.success("You voted for Python!")

elif vote_java:
    st.success("You voted for Java!")

else:
    st.write("Please select a programming language to vote for.")


name = st.sidebar.text_input("Enter your name:")
tea_type = st.sidebar.radio("Select the type of tea you want:", ["Green Tea", "Black Tea", "Herbal Tea"])
st.sidebar.write(f"You have selected {tea_type} tea.")


with st.expander("More Information"):
    st.write("This is a simple Streamlit app that allows users to vote for their favorite programming language and select their preferred type of tea. The app uses columns, buttons, and sidebar inputs to create an interactive user experience.")




