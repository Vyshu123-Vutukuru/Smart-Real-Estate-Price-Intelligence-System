import streamlit as st
import joblib

model = joblib.load("linear_model.pkl")

st.title("🏡 Real Estate Price Predictor")
area = st.number_input("Area (sqft)")
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, step=1)

if st.button("Predict"):
    prediction = model.predict([[area, bedrooms]])
    st.success(f"Estimated Price: ₹{int(prediction[0])}")
