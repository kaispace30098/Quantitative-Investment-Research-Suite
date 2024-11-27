import json
import os
from datetime import datetime
from finvizfinance.news import News

# Function to fetch and save daily news related to a specific company ticker
def fetch_daily_news(ticker, output_dir="data"):
    # Get today's date in the format YYYY-MM-DD
    today = datetime.now().strftime("%Y-%m-%d")

    # Create the subfolder using the ticker name under the 'data' directory (e.g., 'data/AAPL')
    ticker_folder = os.path.join(output_dir, ticker)
    # Create the folder if it doesn't exist
    os.makedirs(ticker_folder, exist_ok=True)

    # Create the filename using today's date
    output_file = os.path.join(ticker_folder, f"{today}_{ticker}_daily_news.json")

    # Create a News object to fetch news
    fnews = News()

    # Fetch the news data
    all_news = fnews.get_news()

    # Ensure 'news' data exists in the response
    if 'news' in all_news:
        # Get the news as a DataFrame
        daily_news = all_news['news']
        
        # Print all news titles for inspection
        print("All news titles fetched:")
        print(daily_news['Title'].tolist())

        # Broader search terms related to Apple
        keywords = [ticker, 'Apple', 'iPhone', 'Mac', 'Tim Cook']
        
        # Filter news by checking if any of the keywords are in the title
        filtered_news = daily_news[daily_news['Title'].str.contains('|'.join(keywords), case=False, na=False)]
        
        # If filtered news exists, save it to JSON
        if not filtered_news.empty:
            filtered_news_list = filtered_news.to_dict(orient='records')

            # Save the filtered news data to a JSON file
            with open(output_file, 'w') as json_file:
                json.dump(filtered_news_list, json_file, indent=4)

            print(f"Daily news related to {ticker} saved to {output_file}")
        else:
            print(f"No relevant news found for {ticker} today.")
    else:
        print("No news data available.")

# Ensure this part of the code only runs when executed directly
if __name__ == "__main__":
    # Specify the company ticker (e.g., 'AAPL' for Apple)
    ticker = "AAPL"
    
    # Call the function to fetch and save news related to the specific ticker
    fetch_daily_news(ticker, output_dir='data')
