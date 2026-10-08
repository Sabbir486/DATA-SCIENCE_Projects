import streamlit as st
import pandas as pd

st.title("Working with DataFrames in Pandas")

df_file = st.file_uploader("Upload a CSV file", type=["csv"])

if df_file:
    df = pd.read_csv(df_file)
    st.subheader("DataFrame Preview")
    st.dataframe(df.head())

if df_file:
    st.subheader("DataFrame Summary")
    st.write(df.describe())

if df_file:
    cities = df['City'].unique()
    selected_city = st.selectbox("Select a city to filter the DataFrame:", cities)
    filtered_df = df[df['City'] == selected_city]
    st.subheader(f"Filtered DataFrame for {selected_city}")
    st.dataframe(filtered_df)