# -*- coding: utf-8 -*-
"""stream.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SNK71SPeAazPMcT54V98mbkT2WtAcT-N
"""

#!pip install streamlit

#from google.colab import drive


# Mount our drive to the working space
#drive.mount('/content/gdrive')

import streamlit as st
import joblib
import pandas as pd
import pickle



# Load the trained model
model = joblib.load('PRICE_OPTIMIZATION/models/jewelry_price_optimizer_linear.pkl')

# Define model metrics (replace with your actual metrics)
METRICS = {
    "Train R²": 0.85,  # Replace with your values
    "Test R²": 0.80,
    "Train RMSE": 10.5,
    "Test RMSE": 12.3,
    "Generalization Error": 1.8
}


def user_input_features():
    st.sidebar.header("Model Performance Metrics")
    for metric, value in METRICS.items():
        st.sidebar.text(f"{metric}: {value:.2f}")

    st.header("Input Features")

    # Numerical inputs
    year = st.number_input("Year", min_value=2018, max_value=2023, value=2020)
    month = st.number_input("Month", min_value=1, max_value=12, value=1)
    hour = st.number_input("Hour", min_value=0, max_value=23, value=12)

    # Main metal selection
    main_metal = st.selectbox("Main Metal", ["None", "platinum", "silver"])
    metal_platinum = (main_metal == "platinum")
    metal_silver = (main_metal == "silver")
    # Add main_metal_unknown if necessary (if model has "unknown" category)

    # Main color selection
    main_color = st.selectbox("Main Color", ["unknown-color", "white", "yellow"])
    color_unknown = (main_color == "unknown-color")
    color_white = (main_color == "white")
    color_yellow = (main_color == "yellow")

    # Gender selection
    gender = st.selectbox("Gender", ["m", "f", "unknown"])
    gender_m = (gender == "m")
    # gender_f = (gender == "f") - Unused as per your feature set

    # Jewelry category
    category = st.selectbox("Category", ["brooch", "earring", "necklace", "pendant", "ring", "souvenir", "stud"])
    cat_brooch = (category == "brooch")
    cat_earring = (category == "earring")
    cat_necklace = (category == "necklace")
    cat_pendant = (category == "pendant")
    cat_ring = (category == "ring")
    cat_souvenir = (category == "souvenir")
    cat_stud = (category == "stud")

    # Brand selection
    brand = st.selectbox("Brand", ["Brand 1", "Brand 2", "Brand 3", "Brand 4", "Brand 5"])
    brand_1 = (brand == "Brand 1")
    brand_2 = (brand == "Brand 2")
    brand_3 = (brand == "Brand 3")
    brand_4 = (brand == "Brand 4")
    brand_5 = (brand == "Brand 5")

    # Create feature dictionary
    features = {
        'Year': year,
        'Month': month,
        'Hour': hour,
        'Main_metal_platinum': metal_platinum,
        'Main_metal_silver': metal_silver,
        'Main_color_unknown-color': color_unknown,
        'Main_color_white': color_white,
        'Main_color_yellow': color_yellow,
        'Gender_m': gender_m,
        'Category_jewelry.brooch': cat_brooch,
        'Category_jewelry.earring': cat_earring,
        'Category_jewelry.necklace': cat_necklace,
        'Category_jewelry.pendant': cat_pendant,
        'Category_jewelry.ring': cat_ring,
        'Category_jewelry.souvenir': cat_souvenir,
        'Category_jewelry.stud': cat_stud,
        'Brand_ID_1.0': brand_1,
        'Brand_ID_2.0': brand_2,
        'Brand_ID_3.0': brand_3,
        'Brand_ID_4.0': brand_4,
        'Brand_ID_5.0': brand_5
    }

    return pd.DataFrame(features, index=[0])

def main():
    st.title("Jewelry Price Prediction")

    input_df = user_input_features()

    if st.button("Predict"):
        prediction = model.predict(input_df)
        st.success(f"Predicted Price: ${prediction[0]:.2f} USD")

if __name__ == "__main__":
    main()

