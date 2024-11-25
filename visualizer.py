import matplotlib.pyplot as plt
import streamlit as st 

def plot_stock_data(data, symbol):
    """
    Plot stock data with Streamlit-compatible visualization
    
    :param data: DataFrame containing stock data
    :param symbol: Stock symbol (e.g., 'AAPL')
        
    """
    if data.empty:
        st.warning("No data available to plot")
        return
    
    plt.figure(figsize=(10,6))
    plt.plot(data['Close'], label='Closing Prices', color='blue')
    
    # Plot any SMA columns in the data
    for column in data.columns:
        if column.startswith("SMA_"):
            plt.plot(data[column],label=column, linestyle='--')
   
    plt.title(f"{symbol} Stock Prices with Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid()
    
    st.pyplot(plt.gcf()) # Streamlit rendering for plots    