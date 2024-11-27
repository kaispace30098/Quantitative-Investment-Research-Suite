import yfinance as yf
import os
from datetime import datetime

# Function to fetch stock data using yfinance
def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    # Fetch stock data for today (1 day period)
    data = stock.history(period="1d", interval="1h")  # 1h interval to get hourly data
    return data

# Function to save stock data into CSV in a specific folder
def save_stock_data(stock_data, ticker, output_dir="data"):
    # Create a subfolder using the ticker name under the 'data' directory (e.g., 'data/AAPL')
    ticker_folder = os.path.join(output_dir, ticker)
    # Ensure the output directory exists
    os.makedirs(ticker_folder, exist_ok=True)
    
    # Get today's date for the filename
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Save to CSV in the ticker's subfolder
    output_file = os.path.join(ticker_folder, f"{today}_{ticker}_stocks.csv")
    
    stock_data.to_csv(output_file)
    print(f"Stock data for {ticker} saved to {output_file}")

if __name__ == "__main__":
    ticker = "AAPL"  # Example ticker (can be replaced)
    stock_data = fetch_stock_data(ticker)
    
    # Call the save function to save stock data to CSV in the ticker subfolder
    save_stock_data(stock_data, ticker)
