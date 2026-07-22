import streamlit as st
import joblib

st.set_page_config(page_title="House Price Predictor")
st.title("🏠 House Price Predictor")

model = joblib.load('house_price_model.pkl')

area = st.slider("Area (sqm)", 50, 300, 150)
bedrooms = st.slider("Bedrooms", 1, 5, 3)
age = st.slider("Age (years)", 0, 50, 10)
proximity = st.slider("Distance to city (km)", 1.0, 10.0, 5.0)

if st.button("Predict Price"):
    pred = model.predict([[area, bedrooms, age, proximity]])[0]
    st.success(f"💰 Predicted Price: ${pred:,.2f}")