import json
import os
from datetime import datetime
from finvizfinance.news import News

# Function to fetch and save daily news with today's date as the filename
def fetch_daily_news(output_dir="data"):
    # Get today's date in the format YYYY-MM-DD
    today = datetime.now().strftime("%Y-%m-%d")

    # Create the filename using today's date
    output_file = os.path.join(output_dir, f"{today}_daily_news.json")

    # Create the 'data' directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Create a News object to fetch news
    fnews = News()

    # Fetch the news data
    all_news = fnews.get_news()

    # Ensure 'news' data exists in the response
    if 'news' in all_news:
        # Get the news as a DataFrame and convert to a dictionary
        daily_news = all_news['news']

        # Convert the news DataFrame to a list of dictionaries
        daily_news_list = daily_news.to_dict(orient='records')

        # Save the data to a JSON file
        with open(output_file, 'w') as json_file:
            json.dump(daily_news_list, json_file, indent=4)

        print(f"Daily news saved to {output_file}")
    else:
        print("No news data available.")

# Ensure this part of the code only runs when executed directly
if __name__ == "__main__":
    # Call the function to fetch and save daily news with today's date as filename
    fetch_daily_news(output_dir='data')
