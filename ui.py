import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="Gold Loan Prediction 💰",
    page_icon="💰",
    layout="centered"
)

# Fancy CSS for blur and background
st.markdown("""
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1607746882042-944635dfe10e?auto=format&fit=crop&w=1950&q=80");
    background-size: cover;
    background-attachment: fixed;
}
.input-container {
    backdrop-filter: blur(10px);
    background-color: rgba(255,255,255,0.3);
    border-radius: 15px;
    padding: 30px;
    box-shadow: 0 8px 32px 0 rgba(0,0,0,0.37);
    margin: auto;
}
.title {
    color: gold;
    font-size: 3rem;
    font-weight: bold;
    text-shadow: 2px 2px 4px black;
    text-align: center;
}
.prediction {
    color: #00FF00;
    font-size: 2rem;
    font-weight: bold;
    text-align: center;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">💰 Gold Loan Price Prediction 💰</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="input-container">', unsafe_allow_html=True)

# API
API = 'http://127.0.0.1:8000/predict'

# Inputs
SPX = st.number_input("S&P 500 Index (SPX)", value=4000.0, step=0.1)
USO = st.number_input("US Oil Fund (USO)", value=80.0, step=0.1)
SLV = st.number_input("Silver Price (SLV)", value=25.0, step=0.1)
EUR_USD = st.number_input("EUR/USD Exchange Rate", value=1.1, step=0.001)
Year = st.number_input("Year", min_value=2000, max_value=2025, value=2025, step=1)

# Predict
if st.button('Predict Now'):
    input_data = {
        'SPX': SPX,
        'USO': USO,
        'SLV': SLV,
        'EUR_USD': EUR_USD,
        'Year': Year
    }
    try:
        response = requests.post(API, json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.markdown(
                f'<div class="prediction">💰 Predicted Gold Loan Price: ₹{result["Predicted_GLD"]:.2f}</div>',
                unsafe_allow_html=True
            )
        else:
            st.error(f"{response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Error connecting to API: {e}")

st.markdown('</div>', unsafe_allow_html=True)
