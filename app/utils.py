import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    # Load the combined cleaned data
    # Ensure this matches the file you created in Task 3
    df = pd.read_csv("data/combined_climate_data.csv")
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    return df

def filter_data(df, countries, year_range):
    filtered = df[
        (df['Country'].isin(countries)) & 
        (df['year'] >= year_range) & 
        (df['year'] <= year_range)
    ]
    return filtered