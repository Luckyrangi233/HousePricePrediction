import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pickle
import os


def train_and_save_model():
    df = pd.DataFrame({
        'area': [1500, 2000, 1700, 2500, 1900],
        'bedrooms': [3, 4, 3, 5, 3],
        'bathrooms': [2, 3, 2, 4, 2],
        'floors': [1, 2, 1, 3, 2],
        'parking': [1, 2, 1, 2, 1],
        'mainroad': [1, 1, 0, 1, 0],
        'furnishing': [0, 2, 1, 2, 0],
        'price': [50, 80, 55, 120, 60]
    })

    X = df.drop('price', axis=1)
    y = df['price']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = LinearRegression()
    model.fit(X_scaled, y)

    os.makedirs("model", exist_ok=True)
    with open("model/house_model.pkl", "wb") as f:
        pickle.dump(model, f)
    with open("model/scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)

# Train model if not already saved
if not os.path.exists("model/house_model.pkl") or not os.path.exists("model/scaler.pkl"):
    train_and_save_model()

# 
model = pickle.load(open("model/house_model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))

st.set_page_config(page_title="House Price Predictor", layout="centered")

st.title("House Price Prediction App")
st.markdown("Enter property features below to estimate the **market price** of the house.")

# Input Form
with st.form("prediction_form"):
    area = st.slider("Area (sq ft)", 500, 10000, 1500)
    bedrooms = st.selectbox("Number of Bedrooms", [1, 2, 3, 4, 5])
    bathrooms = st.selectbox("Number of Bathrooms", [1, 2, 3, 4])
    stories = st.selectbox("Number of Floors", [1, 2, 3])
    parking = st.selectbox("Number of Parking Spots", [0, 1, 2, 3])
    mainroad = st.radio("Is it on the Main Road?", ['Yes', 'No'])
    furnishing = st.radio("Furnishing Status", ['Unfurnished', 'Semi-furnished', 'Furnished'])

    submitted = st.form_submit_button("Predict Price")

# Encode categorical data
mainroad_bin = 1 if mainroad == 'Yes' else 0
furnishing_map = {'Unfurnished': 0, 'Semi-furnished': 1, 'Furnished': 2}
furnishing_encoded = furnishing_map[furnishing]

# Make prediction
if submitted:
    input_features = np.array([[area, bedrooms, bathrooms, stories, parking, mainroad_bin, furnishing_encoded]])
    scaled_input = scaler.transform(input_features)
    predicted_price = model.predict(scaled_input)[0]

    st.success(f"Estimated House Price: ₹ {round(predicted_price, 2)} Lakhs")

    # Display input summary
    st.subheader("Input Summary")
    input_df = pd.DataFrame({
        'Feature': ['Area', 'Bedrooms', 'Bathrooms', 'Floors', 'Parking', 'Main Road', 'Furnishing'],
        'Value': [area, bedrooms, bathrooms, stories, parking, mainroad, furnishing]
    })
    st.table(input_df)
