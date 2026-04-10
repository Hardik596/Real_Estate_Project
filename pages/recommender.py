import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Recommender · PropIQ", page_icon="🔍", layout="wide")

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

.prop-card {
    background: #fff;
    border: 1px solid #e8e4db;
    border-radius: 12px;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
    transition: border-color 0.2s;
}
.prop-card:hover { border-color: #c9a84c; }
.prop-rank {
    width: 32px; height: 32px; border-radius: 50%;
    background: #0d0d0d; color: #fff;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px; font-weight: 600;
    flex-shrink: 0; margin-right: 14px;
}
.prop-name  { font-size: 14px; font-weight: 600; color: #0d0d0d; flex: 1; }
.prop-score { font-size: 15px; font-weight: 700; color: #1a7a6a; }
.prop-score-label { font-size: 10px; color: #7a7a7a; text-align: right; }

.loc-card {
    background: #fff;
    border: 1px solid #e8e4db;
    border-radius: 10px;
    padding: 12px 18px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
    font-size: 14px;
}
.loc-card:hover { border-color: #c9a84c; }
.loc-dist { color: #c9a84c; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# ── Load ───────────────────────────────────────────────────────
location_df = pickle.load(open('location_distance.pkl', 'rb'))
cosine_sim1 = pickle.load(open('cosine_sim1.pkl', 'rb'))
cosine_sim2 = pickle.load(open('cosine_sim2.pkl', 'rb'))
cosine_sim3 = pickle.load(open('cosine_sim3.pkl', 'rb'))

def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 0.5*cosine_sim1 + 0.8*cosine_sim2 + cosine_sim3
    sim_scores   = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices  = [i[0] for i in sorted_scores[1:top_n+1]]
    top_scores   = [i[1] for i in sorted_scores[1:top_n+1]]
    top_properties = location_df.index[top_indices].tolist()
    return pd.DataFrame({'PropertyName': top_properties, 'SimilarityScore': top_scores})

# ── Header ─────────────────────────────────────────────────────
st.markdown("# 🔍 Property Recommender")
st.markdown("Find properties nearby or discover the most similar apartments to any listing.")
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Section 1 — Nearby by radius ──────────────────────────────
st.markdown('<div class="section-label">Location Search</div>', unsafe_allow_html=True)
st.markdown("### Properties within a radius")

col1, col2 = st.columns([2, 1], gap="large")
with col1:
    selected_location = st.selectbox('Select a location', sorted(location_df.columns.to_list()))
with col2:
    radius = st.number_input('Radius (km)', min_value=0.0, max_value=100.0, step=0.5, value=2.0)

if st.button('Search Nearby →'):
    nearby = location_df[location_df[selected_location] <= radius * 1000][selected_location].sort_values()
    if nearby.empty:
        st.info("No properties found within this radius. Try increasing it.")
    else:
        st.markdown(f"**{len(nearby)} properties** found within {radius} km of {selected_location}")
        st.markdown("<br>", unsafe_allow_html=True)
        for name, dist in nearby.items():
            st.markdown(f"""
            <div class="loc-card">
                <span>{name}</span>
                <span class="loc-dist">{dist/1000:.2f} km</span>
            </div>""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Section 2 — Similar apartments ────────────────────────────
st.markdown('<div class="section-label">Similarity Search</div>', unsafe_allow_html=True)
st.markdown("### Similar apartments")

selected_apartment = st.selectbox(
    'Select an apartment',
    sorted(location_df.index.to_list()),
    key='apartment_select'
)

if st.button('Get Recommendations →'):
    recs = recommend_properties_with_scores(selected_apartment, top_n=5)
    st.markdown(f"**Top 5 properties similar to {selected_apartment}**")
    st.markdown("<br>", unsafe_allow_html=True)
    for i, row in recs.iterrows():
        st.markdown(f"""
        <div class="prop-card">
            <div class="prop-rank">{i+1}</div>
            <div class="prop-name">{row['PropertyName']}</div>
            <div style="text-align:right">
                <div class="prop-score">{row['SimilarityScore']:.2f}</div>
                <div class="prop-score-label">similarity</div>
            </div>
        </div>""", unsafe_allow_html=True)
