# House Price Prediction System

This project builds an end-to-end machine learning pipeline to predict housing prices using the California Housing dataset.

## Features
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model comparison (Linear Regression, Random Forest, XGBoost)
- SHAP explainability
- FastAPI prediction API
- Streamlit user interface

## Run the Project

Start API:

uvicorn api.main:app --reload

Start UI:

streamlit run app/streamlit_app.py