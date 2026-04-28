import streamlit as st
import plotly.express as px
from utils import load_data, filter_data

# Page Config for professional look
st.set_page_config(page_title="EthioClimate COP32 Dashboard", layout="wide")

st.title("🌍 African Climate Trends: COP32 Decision Support")
st.markdown("### Strategic Insights for the Ministry of Planning & Development")

# 1. Sidebar Widgets
st.sidebar.header("Filter Settings")
df = load_data()

selected_countries = st.sidebar.multiselect(
    "Select Countries", 
    options=df['Country'].unique(), 
    default=df['Country'].unique()
)

year_range = st.sidebar.slider(
    "Select Year Range", 
    min_value=int(df['year'].min()), 
    max_value=int(df['year'].max()), 
    value=(2015, 2026)
)

variable = st.sidebar.selectbox(
    "Select Variable", 
    options=["T2M", "PRECTOTCORR", "RH2M"], 
    index=0
)

# 2. Process Data
filtered_df = filter_data(df, selected_countries, year_range)

# 3. Visualizations
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"{variable} Trend Over Time")
    fig_line = px.line(
        filtered_df.groupby(['year', 'Country'])[variable].mean().reset_index(),
        x='year', y=variable, color='Country',
        template="plotly_white", title=f"Annual Mean {variable}"
    )
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    st.subheader(f"{variable} Distribution (Boxplot)")
    fig_box = px.box(
        filtered_df, x='Country', y=variable, color='Country',
        template="plotly_white", title=f"Regional Variability in {variable}"
    )
    st.plotly_chart(fig_box, use_container_width=True)

st.info("Source: NASA POWER Data (2015-2026). Prepared by Helen Kokob.")