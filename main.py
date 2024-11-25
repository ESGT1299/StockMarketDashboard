import streamlit as st
import pandas as pd
from data_fetcher import fetch_stock_data
from visualizer import plot_stock_data

# Streamlit app
st.title("Stock Market Analysis Dashboard")

# Input fields
symbol = st.text_input("Enter Stock Symbol (e.g., AAPL)", "AAPL")
start_date = st.date_input("Start Date", value=pd.to_datetime("2023-01-01"))
end_date = st.date_input("End Date", value=pd.to_datetime("2023-12-31"))

# SMA sliders
sma_short = st.slider("Short-Term SMA (days):", min_value=5, max_value=50,value=20, step=1)
sma_long = st.slider("Long-Term SMA (days)", min_value=50, max_value=200, value=50, step=1)

# Fetch and display data
if st.button("Fetch Data"):
    data = fetch_stock_data(symbol, start_date, end_date)
    
    if data.empty:
        st.error("Failed to fetch data. Please check the symbol and data range.")
    else:
        # Add moving averages to the DataFrame
        data[f'SMA_{sma_short}'] = data['Close'].rolling(window=sma_short).mean()
        data[f'SMA_{sma_long}'] = data['Close'].rolling(window=sma_long).mean()
    
    # Display data
    st.write("### Stock Data", data.tail())
    
    
    # Visualize data
    st.write("### Stock Data Chart")
    plot_stock_data(data, symbol)
    