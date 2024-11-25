import yfinance as yf
import pandas as pd

def fetch_stock_data(symbol, start_date, end_date):
    """
    Fetch stock market data for a given symbol and date range
    
    :param symbol: Stock symbol (e.g., "AAPL")
    :param start_date: Start Date (YYYY-MM-DD)
    :param end_date: End Date (YYYY-MM-DD)
    :return: DataFrame containing stock data
    
    """
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(start=start_date, end=end_date)
        return data
    
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()
    
    
    
    stock = yf.Ticker(symbol)
    data = stock.history(start=start_date,end=end_date)
    return data

