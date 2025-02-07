# -*- coding: utf-8 -*-
import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('PRICE_OPTIMIZATION/models/jewelry_price_optimizer_xgb.pkl')

# Define model metrics (replace with your actual metrics)
METRICS = {
    "Train R²": 0.26,
    "Test R²": 0.24,
    "Train RMSE": 392.77,
    "Test RMSE": 342.47,
    "Generalization Error": 50.30
}

# Sidebar navigation
def sidebar_navigation():
    st.sidebar.title("Navigation")
    return st.sidebar.radio("Go to", ["Home","Feature Explanation", "Prediction","Recommendations"])

# Home page content
def home_page():
    st.title("Jewelry Price Optimization")
    st.header("About the Project")
    st.write("""
    This application is designed to assist jewelry businesses in predicting optimal pricing for their products. 
    The project leverages a trained machine learning model to generate price predictions based on various input features, 
    such as metal type, gemstone, brand, and other relevant attributes.
    
    The purpose of this project is to:
    - Help businesses remain competitive in the market.
    - Provide insights for pricing strategies based on historical data and product attributes.
    - Optimize pricing to maximize profit while ensuring customer satisfaction.
    """)
    st.header("How It Works")
    st.write("""
    1. Navigate to the "Prediction" page using the sidebar.
    2. Enter the required product attributes, such as metal type, gemstone, and category.
    3. Click on the "Predict" button to get the optimized price prediction.
    
    This tool is powered by a machine learning model built using historical jewelry sales data. 
    Metrics like R² and RMSE highlight the model's performance, and you can view these in the sidebar.
    """)

# Feature Explanation page
def feature_explanation_page():
    st.title("Feature Explanation")
    st.write("""
    Below is a breakdown of each feature used in the model:
    
    - **Year**: The year the jewelry product was sold.
    - **Month**: The month of sale (1-12). 1 is Jan, 2 is Feb in that order
    - **Hour**: The hour of the day the transaction occurred (0-23).
    - **Main Metal**: The primary metal used in the jewelry (Platinum, Silver, etc.).
    - **Main Color**: The primary color of the jewelry (White, Yellow, Unknown).
    - **Gender**: The target gender for the jewelry (Male, Female, Unknown).
    - **Category**: The type of jewelry (e.g., brooch, earring, necklace, etc.).
    - **Brand**: The brand under which the jewelry is sold (Brand 1, Brand 2, etc.).
    - **Main Gemstone**: The primary gemstone used in the jewelry (e.g., diamond, emerald, ruby, etc.).
    
    Each categorical feature is converted into a one-hot encoded format for model training.
    """)


# Prediction page content
def prediction_page():
    st.sidebar.header("Model Performance Metrics")
    for metric, value in METRICS.items():
        st.sidebar.text(f"{metric}: {value:.2f}")

    st.header("Jewelry Price Prediction")
    input_df = user_input_features()

    if st.button("Predict"):
        prediction = model.predict(input_df)
        st.success(f"Predicted Price: ${prediction[0]:.2f} USD")

# Input features function
def user_input_features():
    st.header("Input Features")
    year = st.number_input("Enter Year", value=2020, step=1)
    month = st.number_input("Month", min_value=1, max_value=12, value=1)
    hour = st.number_input("Hour", min_value=0, max_value=23, value=12)

    main_metal = st.selectbox("Main Metal", ["None", "platinum", "silver"])
    metal_platinum = (main_metal == "platinum")
    metal_silver = (main_metal == "silver")

    main_color = st.selectbox("Main Color", ["unknown-color", "white", "yellow"])
    color_unknown = (main_color == "unknown-color")
    color_white = (main_color == "white")
    color_yellow = (main_color == "yellow")

    gender = st.selectbox("Gender", ["m", "f", "unknown"])
    gender_m = (gender == "m")

    category = st.selectbox("Category", ["brooch", "earring", "necklace", "pendant", "ring", "souvenir", "stud"])
    cat_brooch = (category == "brooch")
    cat_earring = (category == "earring")
    cat_necklace = (category == "necklace")
    cat_pendant = (category == "pendant")
    cat_ring = (category == "ring")
    cat_souvenir = (category == "souvenir")
    cat_stud = (category == "stud")

    brand = st.selectbox("Brand", ["Brand 1", "Brand 2", "Brand 3", "Brand 4", "Brand 5"])
    brand_1 = (brand == "Brand 1")
    brand_2 = (brand == "Brand 2")
    brand_3 = (brand == "Brand 3")
    brand_4 = (brand == "Brand 4")
    brand_5 = (brand == "Brand 5")

    main_gem = st.selectbox(
        "Main Gemstone",
        [
            "amber", "amethyst", "chrysolite", "chrysoprase", "citrine", "coral",
            "corundum_synthetic", "diamond", "emerald", "emerald_geothermal",
            "fianit", "garnet", "garnet_synthetic", "mix", "nacre",
            "nanocrystal", "onyx", "pearl", "quartz", "quartz_smoky",
            "rhodolite", "ruby", "sapphire", "sapphire_geothermal",
            "sitall", "spinel", "topaz", "tourmaline", "turquoise"
        ]
    )
    gem_features = {f"Main_gem_{gem}": (main_gem == gem) for gem in [
        "amber", "amethyst", "chrysolite", "chrysoprase", "citrine", "coral",
        "corundum_synthetic", "diamond", "emerald", "emerald_geothermal",
        "fianit", "garnet", "garnet_synthetic", "mix", "nacre",
        "nanocrystal", "onyx", "pearl", "quartz", "quartz_smoky",
        "rhodolite", "ruby", "sapphire", "sapphire_geothermal",
        "sitall", "spinel", "topaz", "tourmaline", "turquoise"
    ]}

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
        'Brand_ID_5.0': brand_5,
    }
    features.update(gem_features)

    return pd.DataFrame(features, index=[0])


# Recommendations page content
def recommendations_page():
    st.title("Jewelry Pricing Recommendations")

    # Let the user choose one of the four options
    option = st.selectbox(
        "Choose a Pricing Strategy",
        [
            "Moderate Spending, Low Quantity, and Low Frequency",
            "High Spending, Very High Quantity, and High Frequency",
            "High Spending, Moderate Quantity, and Moderate Frequency",
            "General Recommendations"
        ]
    )

    # Show recommendations based on user selection
    if option == "Moderate Spending, Low Quantity, and Low Frequency":
        st.header("Recommendations for Moderate Spending, Low Quantity, and Low Frequency")
        st.write("""
        **Objective:** Increase spending per transaction and encourage more frequent purchases.

        - **Premium Pricing for Exclusive Items:** Position jewelry at a premium price for high-quality or exclusive pieces.
        - **Loyalty Programs:** Introduce rewards-based loyalty programs to incentivize repeat purchases.
        - **Seasonal and Targeted Promotions:** Implement seasonal promotions or personalized offers.
        - **Upselling and Cross-Selling:** Bundle related items and offer them at a slight discount.
        """)

    elif option == "High Spending, Very High Quantity, and High Frequency":
        st.header("Recommendations for High Spending, Very High Quantity, and High Frequency")
        st.write("""
        **Objective:** Maximize the value of large, frequent purchases through volume-based pricing and incentivize continued bulk buying.

        - **Volume-Based Pricing & Bulk Discounts:** Offer wholesale pricing and bulk discounts.
        - **Exclusive Deals for High-Volume Buyers:** Provide exclusive deals like discounts or free shipping for large orders.
        - **Customized Bulk Offerings:** Create special packages for wholesale or business clients.
        - **Subscription Model:** Introduce a subscription service for regular shipments.
        """)

    elif option == "High Spending, Moderate Quantity, and Moderate Frequency":
        st.header("Recommendations for High Spending, Moderate Quantity, and Moderate Frequency")
        st.write("""
        **Objective:** Encourage more frequent purchases while maintaining high-value transactions.

        - **Premium but Accessible Pricing:** Offer jewelry at a premium price but make it accessible for regular purchases.
        - **Bundle Pricing & Volume Discounts:** Provide bundle offers with discounts.
        - **Incentivize Regular Purchases:** Offer loyalty rewards and incentives for repeat purchases.
        - **Exclusive Promotions and Early Access:** Offer early access to new collections.
        """)

    elif option == "General Recommendations":
        st.header("General Recommendations for All Customers")
        st.write("""
        - **Personalized Offers:** Utilize customer data for personalized recommendations.
        - **Flexible Payment Options:** Offer flexible payment plans for high-ticket items.
        - **Customer Education:** Highlight craftsmanship and design to justify premium prices.
        """)
        

# Main function
def main():
    page = sidebar_navigation()
    if page == "Home":
        home_page()
    elif page == "Feature Explanation":
        feature_explanation_page()
    elif page == "Prediction":
        prediction_page()
    elif page == "Recommendations":
        recommendations_page()

if __name__ == "__main__":
    main()
