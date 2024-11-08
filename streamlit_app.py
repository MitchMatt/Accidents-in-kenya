import pandas as pd
import streamlit as st
import sklearn.metrics as metrics
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model


# Load the trained model
model = load_model("deep_learning_model.h5")

# Initialize a StandardScaler instance (load the saved scaler if available)
scaler = StandardScaler()

# Title and description
st.title("Crash Data Prediction App")
st.write("Predicts the probability of crash report based on provided features.")

# User input for model features
n_crash_reports = st.number_input("Number of Crash Reports", min_value=0, step=1)
distance_to_nairobi = st.number_input("Distance to Nairobi (in km)", min_value=0.0)
day_part = st.selectbox("Day Part", ["morning", "afternoon", "evening", "night"])
season = st.selectbox("Season", ["dry", "wet", "transitional"])

# Convert user input to a DataFrame
input_data = pd.DataFrame({
    'n_crash_reports': [n_crash_reports],
    'distance_to_nairobi': [distance_to_nairobi],
    'day_part': [day_part],
    'season': [season]
})

# Preprocess input (One-hot encoding, scaling, etc.)
input_data = pd.get_dummies(input_data)  # Adjust encoding according to your model
input_data = scaler.fit_transform(input_data)  # Use fit_transform if scaler is not pre-fitted

# Make prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write(f"Crash Likelihood: {prediction[0][0]:.2f}")
