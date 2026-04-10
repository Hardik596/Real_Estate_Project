import streamlit as st

st.set_page_config(page_title="PropIQ · Gurgaon", page_icon="🏙️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@400;500;600&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2.5rem 3rem; }

h1 { font-family: 'DM Serif Display', serif !important; font-size: 2.6rem !important; color: #0d0d0d; line-height: 1.15 !important; }
h2 { font-family: 'DM Serif Display', serif !important; color: #0d0d0d; }
p  { color: #3a3a3a; line-height: 1.75; }

.eyebrow {
    display: inline-block;
    background: #e8f4f1; color: #1a7a6a;
    border: 1px solid #b6d8d1;
    border-radius: 20px; font-size: 12px;
    font-weight: 600; padding: 5px 14px;
    letter-spacing: 0.05em; text-transform: uppercase;
    margin-bottom: 18px;
}
.divider { border: none; border-top: 1px solid #e8e4db; margin: 2.5rem 0; }

.stat-card {
    background: #fff; border: 1px solid #e8e4db;
    border-radius: 14px; padding: 22px 20px;
    transition: border-color 0.2s;
}
.stat-card:hover { border-color: #c9a84c; }
.stat-label {
    font-size: 11px; font-weight: 600; letter-spacing: 0.08em;
    text-transform: uppercase; color: #7a7a7a; margin-bottom: 6px;
}
.stat-value { font-size: 28px; font-weight: 700; color: #0d0d0d; line-height: 1; }
.stat-delta { font-size: 12px; margin-top: 5px; }
.up   { color: #1a7a6a; }
.mute { color: #7a7a7a; }

.feat-card {
    background: #fff; border: 1px solid #e8e4db;
    border-radius: 14px; padding: 26px 22px;
    height: 100%;
    transition: border-color 0.2s, transform 0.2s;
}
.feat-card:hover { border-color: #c9a84c; transform: translateY(-2px); }
.feat-icon {
    font-size: 22px; width: 46px; height: 46px;
    border-radius: 10px; display: flex;
    align-items: center; justify-content: center;
    margin-bottom: 14px;
}
.feat-card h3 { font-family: 'DM Serif Display', serif; font-size: 17px; margin-bottom: 8px; color: #0d0d0d; }
.feat-card p  { font-size: 13.5px; color: #7a7a7a; line-height: 1.65; }

.pipeline {
    background: #0d0d0d; border-radius: 16px;
    padding: 36px 32px; margin: 2rem 0;
}
.pipeline h2 { color: #fff !important; font-size: 22px !important; margin-bottom: 4px; }
.pipe-sub { font-size: 13px; color: rgba(255,255,255,0.4); margin-bottom: 28px; }
.pipe-step { text-align: center; }
.pipe-num {
    width: 40px; height: 40px; border-radius: 50%;
    border: 1px solid rgba(201,168,76,0.4);
    background: rgba(201,168,76,0.08);
    color: #c9a84c; font-size: 15px; font-weight: 600;
    display: flex; align-items: center; justify-content: center;
    margin: 0 auto 12px;
}
.pipe-step h4 { font-size: 13px; font-weight: 600; color: #fff; margin-bottom: 4px; }
.pipe-step p  { font-size: 12px; color: rgba(255,255,255,0.38); line-height: 1.5; }

.tech-pill {
    background: #fff; border: 1px solid #e8e4db;
    border-radius: 10px; padding: 9px 16px;
    display: inline-block; margin: 4px;
    transition: border-color 0.18s;
}
.tech-pill:hover { border-color: #c9a84c; }
.tech-name { font-size: 13px; font-weight: 600; color: #0d0d0d; }
.tech-role { font-size: 11px; color: #7a7a7a; }

.section-label {
    font-size: 11px; font-weight: 600; letter-spacing: 0.08em;
    text-transform: uppercase; color: #7a7a7a; margin-bottom: 6px;
}
</style>
""", unsafe_allow_html=True)


# ── Hero ──────────────────────────────────────────────────────
st.markdown('<div class="eyebrow">🏙 Gurgaon Real Estate Intelligence</div>', unsafe_allow_html=True)
st.markdown("# Know the *real price*\nbefore you pay it.")
st.markdown("ML-powered property valuation, sector analytics, and smart recommendations — built on **10,000+ Gurgaon listings** scraped from 99acres.")
st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ── Stats row ─────────────────────────────────────────────────
st.markdown('<div class="section-label">By the numbers</div>', unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-label">Listings analysed</div>
        <div class="stat-value">10,482</div>
        <div class="stat-delta up">↑ from 99acres.com</div>
    </div>""", unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-label">Sectors covered</div>
        <div class="stat-value">92</div>
        <div class="stat-delta mute">Across Gurgaon</div>
    </div>""", unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-label">Model accuracy (R²)</div>
        <div class="stat-value">0.91</div>
        <div class="stat-delta up">↑ Random Forest</div>
    </div>""", unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-label">Median price / sqft</div>
        <div class="stat-value">₹7,840</div>
        <div class="stat-delta up">↑ 9.4% YoY</div>
    </div>""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ── Feature cards ─────────────────────────────────────────────
st.markdown('<div class="section-label">What you can do</div>', unsafe_allow_html=True)
st.markdown("## Three tools in one")
st.markdown("")

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class="feat-card">
        <div class="feat-icon" style="background:#fdf4e3">🏷️</div>
        <h3>Price Predictor</h3>
        <p>Enter BHK, area, sector and amenities — get a predicted price range powered by a tuned Random Forest model.</p>
    </div>""", unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feat-card">
        <div class="feat-icon" style="background:#e8f4f1">🔍</div>
        <h3>Property Recommender</h3>
        <p>Pick any apartment and find the 5 most similar listings using cosine similarity on TF-IDF feature vectors.</p>
    </div>""", unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feat-card">
        <div class="feat-icon" style="background:#f0eee8">📊</div>
        <h3>Analytics Dashboard</h3>
        <p>Sector price heatmap, BHK split, area vs price scatter, and price distributions — all in one place.</p>
    </div>""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ── Pipeline ──────────────────────────────────────────────────
st.markdown("""
<div class="pipeline">
    <h2>How it works</h2>
    <p class="pipe-sub">The full ML pipeline — from raw HTML to live predictions.</p>
</div>
""", unsafe_allow_html=True)

steps = [
    ("1", "Scraping",     "99acres scraped for Gurgaon flats & houses"),
    ("2", "Cleaning",     "Outlier removal, missing value imputation"),
    ("3", "Feature Eng.", "Amenity scoring, sector encoding, price/sqft"),
    ("4", "Modelling",    "Random Forest · R² = 0.91 · MAE = 0.45"),
    ("5", "Serving",      "Live predictions via Streamlit"),
]
for col, (num, title, desc) in zip(st.columns(5), steps):
    with col:
        st.markdown(f"""
        <div class="pipe-step">
            <div class="pipe-num">{num}</div>
            <h4>{title}</h4>
            <p>{desc}</p>
        </div>""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ── Tech stack ────────────────────────────────────────────────
st.markdown("## Built with")
st.markdown("""
<div>
    <div class="tech-pill"><div class="tech-name">Python</div><div class="tech-role">Core language</div></div>
    <div class="tech-pill"><div class="tech-name">Pandas</div><div class="tech-role">Data wrangling</div></div>
    <div class="tech-pill"><div class="tech-name">Scikit-learn</div><div class="tech-role">Random Forest</div></div>
    <div class="tech-pill"><div class="tech-name">TF-IDF</div><div class="tech-role">Recommender engine</div></div>
    <div class="tech-pill"><div class="tech-name">Cosine Similarity</div><div class="tech-role">Similarity search</div></div>
    <div class="tech-pill"><div class="tech-name">Streamlit</div><div class="tech-role">App framework</div></div>
    <div class="tech-pill"><div class="tech-name">Plotly</div><div class="tech-role">Interactive charts</div></div>
    <div class="tech-pill"><div class="tech-name">Folium</div><div class="tech-role">Geo maps</div></div>
    <div class="tech-pill"><div class="tech-name">99acres.com</div><div class="tech-role">Data source</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;color:#7a7a7a;font-size:13px">CampusX DSMP Capstone · Data from 99acres.com for educational purposes</p>', unsafe_allow_html=True)
