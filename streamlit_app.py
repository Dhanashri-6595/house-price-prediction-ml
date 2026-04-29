import streamlit as st
import requests

st.title("🏠 House Price Prediction")

st.write("Enter house details to predict price")

MedInc = st.number_input("Median Income", value=8.3)
HouseAge = st.number_input("House Age", value=25)
AveRooms = st.number_input("Average Rooms", value=6.5)
AveBedrms = st.number_input("Average Bedrooms", value=1.1)
Population = st.number_input("Population", value=1200)
AveOccup = st.number_input("Average Occupancy", value=3.2)
Latitude = st.number_input("Latitude", value=34.2)
Longitude = st.number_input("Longitude", value=-118.4)

if st.button("Predict Price"):

    data = {
        "MedInc": MedInc,
        "HouseAge": HouseAge,
        "AveRooms": AveRooms,
        "AveBedrms": AveBedrms,
        "Population": Population,
        "AveOccup": AveOccup,
        "Latitude": Latitude,
        "Longitude": Longitude
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )

    result = response.json()

    price = result["predicted_price"] * 100000

    st.success(f"Predicted House Price: ${price:,.0f}")