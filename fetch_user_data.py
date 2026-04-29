##Asiwome Agbleze
##CMSC 111/1
##Assignment 1: Fetching Data FROM a REST API

# ==========================================
# Import the requests library so the program
# can send a GET request to the API
# ==========================================
import requests


# ==========================================
# Store the API URL in a variable
# This is the website address the program
# will use to get the user data
# ==========================================
url = "https://jsonplaceholder.typicode.com/users/1"


# ==========================================
# Use a try-except block so the program
# can handle errors without crashing
# ==========================================
try:
    
    # ==========================================
    # Send a GET request to the API
    # ==========================================
    response = requests.get(url)

    # ==========================================
    # Check if the request was successful
    # If the request fails, this will raise
    # an error
    # ==========================================
    response.raise_for_status()

    # ==========================================
    # Convert the JSON response into a Python
    # dictionary using .json()
    # ==========================================
    user_data = response.json()

    # ==========================================
    # Get the name and email from the JSON data
    # ==========================================
    name = user_data["name"]
    email = user_data["email"]

    # ==========================================
    # Print only the user's name and email
    # ==========================================
    print("Name:", name)
    print("Email:", email)


# ==========================================
# Handle errors caused by the request
# such as connection problems or bad status
# codes
# ==========================================
except requests.exceptions.RequestException as e:
    print("Request failed:", e)


# ==========================================
# Handle errors if expected JSON fields
# are missing
# ==========================================
except KeyError:
    print("Error: Could not find name or email in the response.")


# ==========================================
# Handle any other unexpected errors
# ==========================================
except Exception as e:
    print("An unexpected error occurred:", e)