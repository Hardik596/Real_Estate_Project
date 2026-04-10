import streamlit as st
import pickle
import pandas as pd
import numpy as np
from joblib import load


st.set_page_config(page_title="Price Predictor · PropIQ", page_icon="💰", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;500;600&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2.5rem 3rem; }

h1 { font-family: 'DM Serif Display', serif !important; font-size: 2rem !important; color: #0d0d0d; }
h3 { font-family: 'DM Serif Display', serif !important; color: #0d0d0d; }

.section-label {
    font-size: 11px; font-weight: 600; letter-spacing: 0.08em;
    text-transform: uppercase; color: #7a7a7a; margin-bottom: 6px;
}
.divider { border: none; border-top: 1px solid #e8e4db; margin: 2.5rem 0; }

.result-box {
    background: linear-gradient(135deg, #0d0d0d, #1a1a2e);
    border-radius: 16px;
    padding: 40px 32px;
    text-align: center;
    margin-top: 1rem;
}
.result-label {
    font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase;
    color: rgba(255,255,255,0.4); margin-bottom: 10px;
}
.result-price {
    font-family: 'DM Serif Display', serif;
    font-size: 52px; color: #c9a84c;
    line-height: 1; margin-bottom: 10px;
}
.result-range { font-size: 14px; color: rgba(255,255,255,0.38); }
</style>
""", unsafe_allow_html=True)

# ── Load ───────────────────────────────────────────────────────
with open('df.pkl', 'rb') as f:
    df = pickle.load(f)
pipeline = load('pipeline.pkl')
# ── Header ─────────────────────────────────────────────────────
st.markdown("# 💰 Price Predictor")
st.markdown("Enter the property details below to get an estimated market price.")
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Inputs — two columns ───────────────────────────────────────
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown('<div class="section-label">Property</div>', unsafe_allow_html=True)
    property_type = st.selectbox('Property Type',    df['property_type'].unique())
    sector        = st.selectbox('Sector',           sorted(df['sector'].unique()))
    bedRooms      = float(st.selectbox('Bedrooms',   sorted(df['bedRoom'].unique())))
    bathrooms     = float(st.selectbox('Bathrooms',  sorted(df['bathroom'].unique())))
    balcony       = st.selectbox('Balconies',        sorted(df['balcony'].unique()))
    built_up_area = float(st.number_input('Built-up Area (sqft)', min_value=0.0, step=50.0))

with col2:
    st.markdown('<div class="section-label">Details</div>', unsafe_allow_html=True)
    property_age      = st.selectbox('Property Age',      sorted(df['agePossession'].unique()))
    furnishing_status = st.selectbox('Furnishing Status', sorted(df['furnishing_type'].unique()))
    luxury            = st.selectbox('Luxury Category',   sorted(df['luxury_category'].unique()))
    floor_Category    = st.selectbox('Floor Category',    sorted(df['floor_category'].unique()))
    servant_room      = float(st.selectbox('Servant Room', [0.0, 1.0]))
    store_room        = float(st.selectbox('Store Room',   [0.0, 1.0]))

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Predict ────────────────────────────────────────────────────
if st.button('Estimate Price →'):
    if built_up_area <= 0:
        st.warning("Please enter a valid built-up area.")
    else:
        columns   = ['property_type','sector','bedRoom','bathroom','balcony',
                     'agePossession','built_up_area','servant room','store room',
                     'furnishing_type','luxury_category','floor_category']
        input_data = [[property_type, sector, bedRooms, bathrooms, balcony,
                       property_age, built_up_area, servant_room, store_room,
                       furnishing_status, luxury, floor_Category]]
        input_df = pd.DataFrame(input_data, columns=columns)

        predicted_price = np.expm1(pipeline.predict(input_df)[0])
        low_price  = predicted_price - 0.22
        high_price = predicted_price + 0.22

        st.markdown(f"""
        <div class="result-box">
            <div class="result-label">Estimated Market Value</div>
            <div class="result-price">₹{predicted_price:.2f} Cr</div>
            <div class="result-range">Range &nbsp;·&nbsp; ₹{low_price:.2f} Cr — ₹{high_price:.2f} Cr</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Type",    property_type)
        m2.metric("Sector",  sector)
        m3.metric("BHK",     f"{int(bedRooms)} BHK")
        m4.metric("Area",    f"{int(built_up_area)} sqft")
