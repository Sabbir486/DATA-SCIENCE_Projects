import streamlit as st

st.title("Streamlit Layouts")

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

if vote_python:
    st.success("You voted for Python!")

if vote_java:
    st.success("You voted for Java!")

else:
    st.info("Please select a programming language to vote for.")

