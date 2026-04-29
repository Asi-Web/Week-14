## Asiwome Agbleze
## CMSC 111/1
## Assignment 2: Latest_news.py

# ==========================================
# This program uses the GNews API
# It gets the latest headlines and prints
# the title and publication date for each one
# ==========================================


# ==========================================
# Import os to read the API key from an
# environment variable
# Import requests to send the API request
# ==========================================
import os
import requests


# ==========================================
# Create a function to fetch the latest news
# ==========================================
def fetch_latest_news():

    # ==========================================
    # Get the API key from an environment variable
    # The program should not hard-code the key
    # ==========================================
    api_key = os.getenv("NEWS_API_KEY")

    # ==========================================
    # Check if the API key is missing
    # Print the exact required message if missing
    # ==========================================
    if not api_key:
        print("API key not found. Please set your API key.")
        return

    # ==========================================
    # Store the API URL in a variable
    # max=10 asks for at least 10 headlines
    # ==========================================
    url = "https://gnews.io/api/v4/top-headlines"
    params = {
        "category": "general",
        "lang": "en",
        "country": "us",
        "max": 10,
        "apikey": api_key
    }

    # ==========================================
    # Use try-except so the program handles
    # errors without crashing
    # ==========================================
    try:

        # ==========================================
        # Send a GET request to the API
        # ==========================================
        response = requests.get(url, params=params)

        # ==========================================
        # Check if the request was successful
        # If not, print a clear error message
        # ==========================================
        if response.status_code != 200:
            print("Request failed with status code:", response.status_code)
            return

        # ==========================================
        # Convert the response to JSON
        # ==========================================
        data = response.json()

        # ==========================================
        # Get the list of articles from the JSON data
        # ==========================================
        articles = data.get("articles", [])

        # ==========================================
        # Handle the case where no articles are returned
        # ==========================================
        if not articles:
            print("No articles returned.")
            return

        # ==========================================
        # Print each headline title and publication date
        # ==========================================
        count = 0
        for i, article in enumerate(articles, start=1):
            title = article.get("title", "No title found")
            published = article.get("publishedAt", "No date found")

            print(f"{i}. Headline: {title} Published: {published}")
            count += 1

        # ==========================================
        # Print the total number of headlines shown
        # ==========================================
        print(f"Total headlines printed: {count}")

    # ==========================================
    # Handle request-related errors
    # ==========================================
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

    # ==========================================
    # Handle JSON parsing errors
    # ==========================================
    except ValueError:
        print("Error: Could not parse JSON response.")

    # ==========================================
    # Handle any other unexpected errors
    # ==========================================
    except Exception as e:
        print("An unexpected error occurred:", e)


# ==========================================
# Run the function when the file is executed
# ==========================================
if __name__ == "__main__":
    fetch_latest_news()
    