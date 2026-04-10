import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
import ast
from wordcloud import WordCloud
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Analysis · PropIQ", page_icon="📊", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;500;600&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2.5rem 3rem; }

h1 { font-family: 'DM Serif Display', serif !important; font-size: 2rem !important; color: #0d0d0d; }
h2, h3 { font-family: 'DM Serif Display', serif !important; color: #0d0d0d; }

.section-label {
    font-size: 11px; font-weight: 600; letter-spacing: 0.08em;
    text-transform: uppercase; color: #7a7a7a; margin-bottom: 6px;
}
.divider { border: none; border-top: 1px solid #e8e4db; margin: 2.5rem 0; }
</style>
""", unsafe_allow_html=True)

# ── Load data ──────────────────────────────────────────────────
new_df          = pd.read_csv('data_viz1.csv')
feature_text    = pickle.load(open('feature_text.pkl', 'rb'))
sector_features = pickle.load(open('word_cloud_data.pkl', 'rb'))
group_df        = new_df.groupby('sector')[['price','price_per_sqft','built_up_area','latitude','longitude']].mean()

# ── Page header ────────────────────────────────────────────────
st.markdown("# 📊 Market Analysis")
st.markdown("Explore Gurgaon's real estate market — prices, amenities, BHK trends, and distributions.")
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Viz 1 — Geo map ────────────────────────────────────────────
st.markdown('<div class="section-label">Price Intelligence</div>', unsafe_allow_html=True)
st.markdown("### Price per Sqft · Sector Map")

fig = px.scatter_mapbox(
    group_df, lat='latitude', lon='longitude',
    color='price_per_sqft', size='built_up_area',
    color_continuous_scale=px.colors.cyclical.IceFire,
    zoom=10, mapbox_style="open-street-map",
    text=group_df.index, hover_name=group_df.index,
    height=550,
)
fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
st.plotly_chart(fig, use_container_width=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Viz 2 — Word cloud ─────────────────────────────────────────
st.markdown('<div class="section-label">Amenity Insights</div>', unsafe_allow_html=True)
st.markdown("### Sector Amenity Word Cloud")

selected_sector = st.selectbox(
    "Select a sector",
    options=sector_features['sector_y'].unique(),
    key='sector_select'
)

def make_wordcloud_text(sector):
    rows = sector_features[sector_features['sector_y'] == sector]
    words = []
    for item in rows['features'].dropna().apply(ast.literal_eval):
        words.extend(item)
    return ' '.join(words)

wc = WordCloud(
    width=900, height=380,
    background_color='white',
    stopwords={'s'},
    min_font_size=10
).generate(make_wordcloud_text(selected_sector))

fig2, ax = plt.subplots(figsize=(11, 4))
fig2.patch.set_facecolor('#faf8f4')
ax.imshow(wc, interpolation='bilinear')
ax.axis("off")
plt.tight_layout(pad=0)
st.pyplot(fig2)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Viz 3 — Area vs Price ──────────────────────────────────────
st.markdown('<div class="section-label">Size & Price</div>', unsafe_allow_html=True)
st.markdown("### Area vs Price")

property_type = st.selectbox(
    "Select property type",
    options=new_df['property_type'].unique(),
    key='property_type_select'
)

fig3 = px.scatter(
    new_df[new_df['property_type'] == property_type],
    x='built_up_area', y='price', color='bedRoom',
    labels={'built_up_area': 'Built-up Area (sqft)', 'price': 'Price (Cr)', 'bedRoom': 'BHK'},
    height=450,
)
fig3.update_layout(plot_bgcolor='#faf8f4', paper_bgcolor='#faf8f4')
st.plotly_chart(fig3, use_container_width=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Viz 4 — BHK pie ────────────────────────────────────────────
st.markdown('<div class="section-label">Configuration Split</div>', unsafe_allow_html=True)
st.markdown("### BHK Distribution")

sector_ops = ['Overall'] + sorted(new_df['sector'].unique().tolist())
selected_sector_pie = st.selectbox('Select sector', sector_ops, key='pie_sector')

pie_df = new_df if selected_sector_pie == 'Overall' else new_df[new_df['sector'] == selected_sector_pie]

fig4 = px.pie(
    pie_df, names='bedRoom', hole=0.4,
    color_discrete_sequence=['#1a7a6a','#c9a84c','#e8e4db','#0f3460','#c94f3a'],
    height=420,
)
st.plotly_chart(fig4, use_container_width=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Viz 5 — BHK price box ──────────────────────────────────────
st.markdown('<div class="section-label">Price Comparison</div>', unsafe_allow_html=True)
st.markdown("### BHK Price Range")

fig5 = px.box(
    new_df[new_df['bedRoom'] <= 4],
    x='bedRoom', y='price', color='bedRoom',
    labels={'bedRoom': 'BHK', 'price': 'Price (Cr)'},
    color_discrete_sequence=['#1a7a6a','#c9a84c','#0f3460','#c94f3a'],
    height=420,
)
fig5.update_layout(showlegend=False, plot_bgcolor='#faf8f4', paper_bgcolor='#faf8f4')
st.plotly_chart(fig5, use_container_width=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Viz 6 — House vs Flat distribution ────────────────────────
st.markdown('<div class="section-label">Property Type</div>', unsafe_allow_html=True)
st.markdown("### Price Distribution · House vs Flat")

fig6, ax6 = plt.subplots(figsize=(11, 4))
fig6.patch.set_facecolor('#faf8f4')
ax6.set_facecolor('#faf8f4')
sns.kdeplot(new_df[new_df['property_type'] == 'house']['price'], label='House', color='#1a7a6a', fill=True, alpha=0.25, ax=ax6)
sns.kdeplot(new_df[new_df['property_type'] == 'flat']['price'],  label='Flat',  color='#c9a84c', fill=True, alpha=0.25, ax=ax6)
ax6.set_xlabel('Price (Cr)', fontsize=12)
ax6.spines[['top', 'right']].set_visible(False)
ax6.legend()
st.pyplot(fig6)
