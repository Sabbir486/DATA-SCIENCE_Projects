import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal
from fastapi.middleware.cors import CORSMiddleware

model = joblib.load('Mental_Health_Model.pkl')
app = FastAPI()     # Creating an Object

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# First PyDantic Model
class StudentData(BaseModel):
    Age                     : int = Field(..., gt=10, le=100)
    Gender                  : Literal['Male', 'Female']
    Country                 : str
    Academic_Level          : Literal['High School', 'Undergraduate', 'Graduate']
    Most_Used_Platform      : Literal['Instagram', 'Facebook', 'Twitter', 'Snapchat', 'TikTok', 'YouTube', 'Reddit','LinkedIn', 'LINE', 'WhatsApp', 'WeChat', 'KakaoTalk', 'VKontakte']
    Purpose_Of_Use          : Literal['Networking', 'Entertainment', 'Education', 'News']
    Avg_Daily_Usage_Hours   : float = Field(..., gt=0, le=24)
    Daily_Unlocks           : int   = Field(..., gt=0, le=100)
    Study_Hours             : float = Field(..., gt=0, le=24)
    Physical_Activity_Hours : float = Field(..., gt=0, le=24)
    Sleep_Hours_Per_Night   : float = Field(..., gt=0, le=24)
    Stress_Level            : Literal['Low', 'Medium', 'High', 'Very High']


# Describe what we send back to the user
class PredictionResponse(BaseModel):
    prediction: float


@app.get("/")
def greet():
    return {"message": "Welcome to the Mental Health API"}


top_countries = ['Other ', 'India', 'USA', 'Canada', 'Australia', 'UK', 'Germany', 'Mexico', 'Turkey', 'France']

@app.post("/predict", response_model=PredictionResponse)
def predict(data: StudentData):

    # Group the countries
    country_group = data.Country if data.Country in top_countries else 'Other'

    input_row = pd.DataFrame([{
        'Age': data.Age,
        'Gender': data.Gender,
        'Country': data.Country,
        'Academic_Level': data.Academic_Level,
        'Most_Used_Platform': data.Most_Used_Platform,
        'Purpose_Of_Use': data.Purpose_Of_Use,
        'Avg_Daily_Usage_Hours': data.Avg_Daily_Usage_Hours,
        'Daily_Unlocks': data.Daily_Unlocks,
        'Study_Hours': data.Study_Hours,
        'Physical_Activity_Hours': data.Physical_Activity_Hours,
        'Sleep_Hours_Per_Night': data.Sleep_Hours_Per_Night,
        'Stress_Level': data.Stress_Level,
        'Grouped_Country': country_group
    }])  



    prediction = model.predict(input_row)[0]
    return PredictionResponse(prediction = round(float(prediction), 2))