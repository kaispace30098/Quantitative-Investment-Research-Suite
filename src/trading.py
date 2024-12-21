from dotenv import load_dotenv
import os
from alpaca_trade_api.rest import REST

# Load environment variables from the .env file
load_dotenv()  # This assumes the .env file is in the current working directory

# Retrieve API credentials from environment variables
API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
BASE_URL = os.getenv("ALPACA_BASE_URL")

# Check if the variables are loaded correctly
print(API_KEY)
print(SECRET_KEY)
print(BASE_URL)

# Initialize Alpaca REST client
client = REST(API_KEY, SECRET_KEY, base_url=BASE_URL)

# Fetch account details
account = client.get_account()

# Print account information
print("Account Info:")
print(f"ID: {account.id}")
print(f"Equity: {account.equity}")
print(f"Cash: {account.cash}")