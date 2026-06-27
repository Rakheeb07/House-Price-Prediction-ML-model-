import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("🏠 House Price Prediction")
st.write("Enter the house details below to predict the price.")

# Numeric Inputs
area = st.number_input("Area (sq ft)", min_value=500, max_value=20000, value=5000)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
stories = st.number_input("Stories", min_value=1, max_value=5, value=2)
parking = st.number_input("Parking Spaces", min_value=0, max_value=5, value=1)

# Yes/No Inputs
mainroad = st.selectbox("Main Road", ["Yes", "No"])
guestroom = st.selectbox("Guest Room", ["Yes", "No"])
basement = st.selectbox("Basement", ["Yes", "No"])
hotwater = st.selectbox("Hot Water Heating", ["Yes", "No"])
airconditioning = st.selectbox("Air Conditioning", ["Yes", "No"])
prefarea = st.selectbox("Preferred Area", ["Yes", "No"])

# Furnishing Status
furnishing = st.selectbox(
    "Furnishing Status",
    ["Furnished", "Semi-Furnished", "Unfurnished"]
)

semi = 1 if furnishing == "Semi-Furnished" else 0
unfurnished = 1 if furnishing == "Unfurnished" else 0

# Create DataFrame
input_data = pd.DataFrame({
    "area": [area],
    "bedrooms": [bedrooms],
    "bathrooms": [bathrooms],
    "stories": [stories],
    "mainroad": [1 if mainroad == "Yes" else 0],
    "guestroom": [1 if guestroom == "Yes" else 0],
    "basement": [1 if basement == "Yes" else 0],
    "hotwaterheating": [1 if hotwater == "Yes" else 0],
    "airconditioning": [1 if airconditioning == "Yes" else 0],
    "parking": [parking],
    "prefarea": [1 if prefarea == "Yes" else 0],
    "furnishingstatus_semi-furnished": [semi],
    "furnishingstatus_unfurnished": [unfurnished]
})

# Prediction
if st.button("Predict House Price"):
    prediction = model.predict(input_data)[0]

    st.success(f"Predicted House Price: ₹ {prediction:,.2f}")
