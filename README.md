House Price Prediction System

An end-to-end machine learning system for predicting house prices using the California Housing dataset.
The project includes data analysis, feature engineering, model training, explainability, API deployment, and a web interface.

Project Overview

This project builds a regression-based machine learning model to estimate house prices based on housing features such as:

Median income
House age
Average number of rooms
Population
Geographic location

The system compares multiple models and deploys the best-performing model using an API and an interactive user interface.

Features
Exploratory Data Analysis (EDA)
Feature Engineering
Model Comparison
Linear Regression
Random Forest
XGBoost
Model Explainability using SHAP
REST API using FastAPI
Interactive UI using Streamlit
Model persistence using Joblib
Project Architecture
User Input
    ↓
Streamlit Web Interface
    ↓
FastAPI Prediction API
    ↓
Feature Engineering
    ↓
StandardScaler
    ↓
XGBoost Model
    ↓
Predicted House Price
Model Performance
Model	RMSE	R² Score
Linear Regression	0.59	0.62
Random Forest	0.46	0.77
XGBoost	0.42	0.81

XGBoost provided the best predictive performance and was selected for deployment.

Technologies Used
Python
Pandas
NumPy
Scikit-learn
XGBoost
SHAP
FastAPI
Streamlit
Matplotlib / Seaborn
Project Structure
house-price-prediction-ml
│
├── api
│   └── main.py                # FastAPI prediction API
│
├── app
│   └── streamlit_app.py      # Streamlit web interface
│
├── src
│   ├── train.py              # Model training script
│   ├── predict.py            # Prediction logic
│   └── preprocessing.py      # Data preprocessing
│
├── models
│   ├── house_price_model.pkl
│   └── scaler.pkl
│
├── notebooks
│   └── eda.ipynb             # Data analysis notebook
│
├── README.md
└── requirements.txt
Installation

Clone the repository:

git clone https://github.com/Dhanashri-6595/house-price-prediction-ml.git
cd house-price-prediction-ml

Install dependencies:

pip install -r requirements.txt
Running the Project

Start the API server:

uvicorn api.main:app --reload

The API will run at:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs

Start the Streamlit web application:

streamlit run app/streamlit_app.py

The interface will open at:

http://localhost:8501
Example Prediction

Input:

Median Income: 8.3
House Age: 25
Average Rooms: 6.5
Population: 1200

Predicted house price:

$370,000
Future Improvements
Hyperparameter optimization
Docker containerization
Cloud deployment
CI/CD pipeline
Model monitoring
Author

Dhanashri Magdum
Machine Learning & AI Enthusiast

GitHub:
https://github.com/Dhanashri-6595
