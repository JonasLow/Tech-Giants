import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import sys

# Define company symbols
google_symbol = "GOOG"
amazon_symbol = "AMZN"

# Function to get historical data using yfinance
def get_historical_data(symbol):
    stock = yf.Ticker(symbol)
    historical_data = stock.history(period="max")
    return historical_data

# Function to get current market capitalization using yfinance
def get_market_cap(symbol):
    stock = yf.Ticker(symbol)
    info = stock.info
    return info.get("marketCap", "N/A")

# Download historical financial data
try:
    google_data = get_historical_data(google_symbol)
    amazon_data = get_historical_data(amazon_symbol)
except Exception as e:
    print(f"Error fetching historical data: {e}")
    sys.exit(0)
    # Handle the error or exit gracefully

# Data validation
if google_data.empty or amazon_data.empty:
    print("Error: No data available.")
    # Handle the error or exit gracefully

# Calculate estimated revenue based on daily average price and volume
google_revenue = google_data["Close"] * google_data["Volume"]
amazon_revenue = amazon_data["Close"] * amazon_data["Volume"]

# Print results
print(f"Google average daily revenue: {google_revenue.mean()}")
print(f"Amazon average daily revenue: {amazon_revenue.mean()}")

google_market_cap = get_market_cap(google_symbol)
amazon_market_cap = get_market_cap(amazon_symbol)

# Print results
print(f"Google market capitalization: {google_market_cap}")
print(f"Amazon market capitalization: {amazon_market_cap}")

# Visualization using Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(google_data.index, google_data["Close"], label="Google Close Price", color="blue")
plt.plot(amazon_data.index, amazon_data["Close"], label="Amazon Close Price", color="green")
plt.title("Google and Amazon Stock Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.legend()
plt.show()