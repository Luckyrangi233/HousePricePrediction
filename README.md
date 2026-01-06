# 🏠 House Price Prediction

A Streamlit web app that predicts house prices using a trained machine learning model.

<img width="1200" height="838" alt="Screenshot 2025-09-03 000311" src="https://github.com/user-attachments/assets/2a14b457-4316-4a42-b4d1-0824d77ee55b" />

<img width="1133" height="613" alt="Screenshot 2025-09-15 121334" src="https://github.com/user-attachments/assets/7074cbe8-89cf-4c15-9913-6a3c5b456080" />

This project predicts the price of a house based on various property features using a trained machine learning model, deployed with Streamlit.

📌 Project Overview

The House Price Prediction system uses a supervised machine learning regression model to estimate house prices from user-provided house details.
The model is trained on a housing dataset and served through an interactive Streamlit web application.

🧠 Features Used in Prediction

Area / Square Footage – Total size of the house

Bedrooms – Number of bedrooms

Bathrooms – Number of bathrooms

Floors – Number of floors

Year Built – Construction year of the house

Location-based Features – Encoded numerical values representing location

Additional Numerical Features – Scaled or transformed inputs

Note:
Some feature values may be normalized or scaled, so they may not appear in their original units.

⚙️ How Prediction Works

You can use the app in two ways:

🔹 1. Manual Prediction

Enter house details using Streamlit input widgets

Click Predict Price

The model displays the estimated house price instantly

🔹 2. CSV File Prediction

Upload a CSV file containing multiple house records

The CSV must contain all required feature columns

The app predicts prices for all houses at once and displays the results

📊 Output

Single Prediction: Displays predicted house price on the screen

Batch Prediction: Shows a table with predicted prices

Option to download prediction results as a CSV file

🏗️ Tech Stack

Frontend & Backend: Streamlit

Model: Machine Learning Regression Model

Language: Python

Libraries: NumPy, Pandas, Scikit-learn

▶️ Run Locally
1️⃣ Create Virtual Environment
python -m venv venv


Activate it:

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Git Bash / CMD
.\venv\Scripts\activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py

📁 Project Structure
HousePricePrediction/
│
├── app.py                  # Streamlit application
├── model/
│   ├── model.pkl           # Trained ML model
│   └── scaler.pkl          # Feature scaler
├── dataset/
│   └── housing_sample.csv  # Sample CSV file
├── uploads/                # Optional CSV outputs
├── requirements.txt        # Python dependencies
└── README.md

⚠️ Notes

This project is created for learning and demonstration purposes

Replace the model with one trained on a real-world housing dataset for better accuracy

Proper feature engineering improves prediction performance

📌 Model Output

Predicted Value: Estimated house price (continuous value)

Regression-based prediction (not classification)

⭐ Repository Name
# HousePricePrediction

## 🚀 How to Run Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/House_Price_Prediction.git
cd House_Price_Prediction
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

