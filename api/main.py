from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="House Price Prediction API")

model = joblib.load("house_price_model.pkl")
scaler = joblib.load("scaler.pkl")


class HouseData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float


@app.get("/")
def home():
    return {"message": "House Price Prediction API is running"}


@app.post("/predict")
def predict(data: HouseData):
    rooms_per_household = data.AveRooms / data.AveOccup
    bedrooms_per_room = data.AveBedrms / data.AveRooms
    population_per_household = data.Population / data.AveOccup

    features = np.array([[
        data.MedInc,
        data.HouseAge,
        data.AveRooms,
        data.AveBedrms,
        data.Population,
        data.AveOccup,
        data.Latitude,
        data.Longitude,
        rooms_per_household,
        bedrooms_per_room,
        population_per_household
    ]])

    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)

    return {"predicted_price": float(prediction[0])}