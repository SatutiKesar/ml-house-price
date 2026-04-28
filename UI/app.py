import streamlit as st
import requests
import json

# Page config
st.set_page_config(page_title="House Price Predictor", layout="centered")

# Background CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #1f4037, #99f2c8);
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">House Price Predictor</div>', unsafe_allow_html=True)

# Load locations from JSON
with open("../server/artifacts/columns.json", "r") as f:
    data = json.load(f)
    locations = data["data_columns"][3:]  # skip sqft, bath, bhk

# UI layout
st.write("### Enter Property Details")

location = st.selectbox("Select Location", sorted(locations))
sqft = st.slider("Total Sqft", 300, 10000, 1000)
bath = st.slider("Bathrooms", 1, 10, 2)
bhk = st.slider("BHK", 1, 10, 2)

# Predict button
if st.button("Predict Price"):
    url = "http://127.0.0.1:8000/predict"

    payload = {
        "location": location,
        "total_sqft": sqft,
        "bath": bath,
        "bhk": bhk
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        result = response.json()
        # st.success(f"Estimated Price: ₹ {result['predicted_price']} Lakhs")
        price = round(result["predicted_price"], 2)

        st.markdown(f"""
            <h3 style='color:#000000; text-align:center; background-color:white; padding:10px; border-radius:8px;'>
            Estimated Price: ₹ {price} Lakhs
            </h3>
""", unsafe_allow_html=True)

    else:
        st.error("❌ API Error. Check FastAPI server.")



