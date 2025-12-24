from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle
from fastapi.responses import JSONResponse

# Load model & scaler
with open('GoldLoanModel.pkl','rb') as f:
    model = pickle.load(f)

with open('scaler.pkl','rb') as f:
    scaler = pickle.load(f)

app = FastAPI(title="Gold Loan Prediction API")

# Input validation
class GoldLoanInput(BaseModel):
    SPX: float
    USO: float
    SLV: float
    EUR_USD: float
    Year: int

@app.post('/predict')
def predict(data: GoldLoanInput):
    # Make DataFrame with correct column names
    input_df = pd.DataFrame([{
        'SPX': data.SPX,
        'USO': data.USO,
        'SLV': data.SLV,
        'EUR/USD': data.EUR_USD,  # must match training
        'Year': data.Year
    }])

    # Scale input
    input_scaled = scaler.transform(input_df)

    # Predict
    prediction = model.predict(input_scaled)[0]

    # Clip negative predictions
    prediction = max(0, prediction)

    return JSONResponse(content={"Predicted_GLD": prediction})

@app.get('/')
def home():
    return {"message": "Welcome to Gold Loan Prediction API."}
