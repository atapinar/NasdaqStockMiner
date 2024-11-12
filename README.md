# Nasdaq Stock Miner

## Code Explanation
This Python script fetches historical stock data, calculates key financial indicators (Log Returns, Volatility, RSI), and visualizes them for a specified list of U.S. stock symbols.

## Key Sections of the Code:
1. Library Imports and Setup:

* We import necessary libraries including ```numpy``` for numerical operations, ```pandas``` for data manipulation, ```yfinance``` for stock data retrieval, ```matplotlib``` for plotting, and ```datetime``` for date manipulation.
* ```pytz``` is imported to handle time zone information if needed in date calculations.

2. ```get_stock_data``` Function:

This function retrieves stock data for a given symbol over a specified date range using the ```yfinance``` library.
It calculates the daily logarithmic return (```Log_Ret```), a 30-day rolling standard deviation for volatility (```Volatility```), and the 14-day Relative Strength Index (```RSI```), a common technical indicator for identifying overbought and oversold conditions.
It uses the formula for RSI, which compares the average gains to average losses over a 14-day period.

3. User Input and Date Setup:

* The script prompts the user to enter one or more stock symbols (e.g., "AAPL, MSFT").
* The current date is used as the end date, and the start date is set to one year prior to fetch one year of data for each stock symbol entered.

4. Fetching Data and Handling Errors:

* For each stock symbol, get_stock_data is called to download data within the specified date range.
* If no data is found or if an error occurs, the script skips the symbol with a message output to notify the user.

5. Data Visualization:

* For each stock with data, the script generates three plots:
1. Closing Price: A line plot of daily closing prices.
2. 30-Day Rolling Volatility: A line plot showing the rolling volatility over time, which helps indicate how the stock's volatility changes.
3. Relative Strength Index (RSI): A line plot for the RSI, with horizontal lines at 70 and 30 to highlight overbought (above 70) and oversold (below 30) conditions.
* Each plot is labeled and displayed in a 3-row subplot arrangement for a clean visual summary of each stock's performance over the past year.

## Additional Notes:
* This script is designed for quick data visualization and analysis, making it suitable for traders, analysts, and enthusiasts interested in monitoring stock performance and technical indicators.
* Before running, ensure you have the necessary libraries installed. You can install them via:
```
pip install numpy pandas yfinance matplotlib
```
