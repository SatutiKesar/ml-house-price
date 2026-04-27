from fastapi import FastAPI
import pickle
import json
import numpy as np
import os
from pydantic import BaseModel

app = FastAPI()

# paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "artifacts/banglore_home_prices_model.pickle")
columns_path = os.path.join(BASE_DIR, "artifacts/columns.json")

# load model
with open(model_path, "rb") as f:
    model = pickle.load(f)

# load columns
with open(columns_path, "r") as f:
    data_columns = json.load(f)["data_columns"]

# input schema
class HouseData(BaseModel):
    location: str
    total_sqft: float
    bath: int
    bhk: int

@app.get("/")
def home():
    return {"message": "House Price Prediction API running"}

def predict_price(location, sqft, bath, bhk):
    x = np.zeros(len(data_columns))
    
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if location.lower() in data_columns:
        loc_index = data_columns.index(location.lower())
        x[loc_index] = 1

    return model.predict([x])[0]

@app.post("/predict")
def predict(data: HouseData):
    price = predict_price(
        data.location,
        data.total_sqft,
        data.bath,
        data.bhk
    )
    return {"predicted_price": round(price, 2)}
