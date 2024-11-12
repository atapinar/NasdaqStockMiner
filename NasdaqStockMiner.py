# Script 1: Input Stocks Closing Prices, Volatility, and RSI Plots

import sys
print("Python executable being used:", sys.executable)

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pytz  # Import pytz for timezone handling

# Function to retrieve and process stock data
def get_stock_data(symbol, start_date, end_date):
    """
    Retrieves stock data from Yahoo Finance and calculates log returns, rolling volatility, and RSI.

    Parameters:
    - symbol (str): Stock ticker symbol.
    - start_date (str): Start date in 'YYYY-MM-DD' format.
    - end_date (str): End date in 'YYYY-MM-DD' format.

    Returns:
    - pd.DataFrame: DataFrame containing stock data with log returns, volatility, and RSI.
    """
    try:
        # Retrieve stock data using yfinance
        stock = yf.download(symbol, start=start_date, end=end_date, progress=False)
        
        # Check if data was retrieved successfully
        if stock.empty:
            print(f"No data found for symbol: {symbol}\n")
            return None
        
        # Calculate the log returns
        stock['Log_Ret'] = np.log(stock['Close'] / stock['Close'].shift(1))
        
        # Calculate the rolling volatility with a window of 30 days
        stock['Volatility'] = stock['Log_Ret'].rolling(window=30).std() * np.sqrt(252)
        
        # Calculate RSI with a window of 14 days
        delta = stock['Close'].diff()
        gain = (delta.where(delta > 0, 0)).fillna(0)
        loss = (-delta.where(delta < 0, 0)).fillna(0)
        window = 14
        avg_gain = gain.rolling(window=window, min_periods=window).mean()
        avg_loss = loss.rolling(window=window, min_periods=window).mean()
        rs = avg_gain / avg_loss
        stock['RSI'] = 100 - (100 / (1 + rs))
        
        return stock
    except Exception as e:
        print(f"An error occurred while fetching data for {symbol}: {e}\n")
        return None

# ----- Input Section -----
user_input = input("Enter US stock symbols separated by commas (e.g., AAPL, MSFT, AMZN): ")
stock_symbols = [symbol.strip().upper() for symbol in user_input.split(',')]

# Define the dynamic 1-year date range
end_date = datetime.now()
start_date = end_date - timedelta(days=365)
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')

print(f"\nFetching data from {start_date_str} to {end_date_str}...\n")

# Retrieve and process data for each stock symbol
stock_data = {}
for symbol in stock_symbols:
    print(f"Fetching data for {symbol}...")
    data = get_stock_data(symbol, start_date_str, end_date_str)
    if data is not None:
        print(f"Data fetched for {symbol}.\n")
        stock_data[symbol] = data
    else:
        print(f"Skipping {symbol} due to data retrieval issues.\n")

# ----- Plotting Stock Closing Prices, Volatility, and RSI (Last 1 Year) -----
for symbol, data in stock_data.items():
    try:
        fig, ax = plt.subplots(3, 1, figsize=(14, 15), sharex=True)
        
        # Plot Closing Prices
        ax[0].plot(data.index, data['Close'], label=f'{symbol} Close Price', color='blue')
        ax[0].set_title(f'{symbol} Closing Prices (Last 1 Year)')
        ax[0].set_ylabel('Price (USD)')
        ax[0].legend()
        
        # Plot Rolling Volatility
        ax[1].plot(data.index, data['Volatility'], label=f'{symbol} 30-Day Rolling Volatility', color='orange')
        ax[1].set_title(f'{symbol} Rolling Volatility (Last 1 Year)')
        ax[1].set_ylabel('Volatility')
        ax[1].legend()
        
        # Plot RSI
        ax[2].plot(data.index, data['RSI'], label=f'{symbol} RSI (14)', color='green')
        ax[2].axhline(70, color='red', linestyle='--', linewidth=1)
        ax[2].axhline(30, color='red', linestyle='--', linewidth=1)
        ax[2].set_title(f'{symbol} Relative Strength Index (RSI) (Last 1 Year)')
        ax[2].set_ylabel('RSI')
        ax[2].set_xlabel('Date')
        ax[2].legend()
        
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"An error occurred while plotting data for {symbol}: {e}\n")
