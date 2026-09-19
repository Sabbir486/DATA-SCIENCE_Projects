import streamlit as st
import pandas as pd
import joblib

model = joblib.load("logistic_regression_model.pkl")
scaler = joblib.load("scaler.pkl")
features = joblib.load("features.pkl")

st.title("Heart Disease Prediction App ❤️")
st.markdown("Provide the following information:")

age = st.number_input("Age", min_value=15, max_value=100, value=30)
sex = st.selectbox("Gender", ["Male", "Female"])
chest_pain_type = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
resting_bp = st.number_input("Resting Blood Pressure", min_value=70, max_value=200, value=120)
cholesterol = st.number_input("Cholesterol", min_value=100, max_value=600, value=200)
fasting_blood_sugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.slider("Maximum Heart Rate", min_value=60, max_value=200, value=150)
exercise_angina = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=1.0)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

if st.button("Predict"):

    raw_data = {
        "Age": age,
        "Sex": 1 if sex == "Male" else 0,
        "ChestPainType": chest_pain_type,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": 1 if fasting_blood_sugar == "Yes" else 0,
        "RestingECG": resting_ecg,
        "MaxHR": max_hr,
        "ExerciseAngina": 1 if exercise_angina == "Yes" else 0,
        "Oldpeak": oldpeak,
        "ST_Slope": st_slope
    }

    input_df = pd.DataFrame([raw_data])

    input_df = pd.get_dummies(
        input_df,
        columns=["ChestPainType", "RestingECG", "ST_Slope"],
        dtype=int
    )

    input_df = input_df.reindex(
        columns=features,
        fill_value=0
    )

    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.error("The model predicts that you have heart disease. Please consult a doctor.")
    else:
        st.success("The model predicts that you do not have heart disease.")