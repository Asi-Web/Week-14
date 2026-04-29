## Asiwome Agbleze3
## CMSC 111/1
## Asignment 3: Fetch and Parse JSON Data (TODO Titles)

# ==========================================
# Import the requests library so the program
# can send an HTTP GET request to the API
# ==========================================
import requests


# ==========================================
# Store the API URL in a variable
# This is the endpoint that returns the todo list
# ==========================================
url = "https://jsonplaceholder.typicode.com/todos"


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
    # Status code 200 means success
    # ==========================================
    if response.status_code == 200:

        # ==========================================
        # Convert the JSON response into Python data
        # The API returns a list of todo objects
        # ==========================================
        todos = response.json()

        # ==========================================
        # Set a counter for how many titles are printed
        # ==========================================
        count = 0

        # ==========================================
        # Loop through the first 20 todo items
        # and print the value of the title field
        # ==========================================
        for i, todo in enumerate(todos[:20], start=1):
            title = todo.get("title", "No title found")
            print(f"{i}. {title}")
            count += 1

        # ==========================================
        # Print the total number of titles printed
        # ==========================================
        print(f"Total titles printed: {count}")

    else:
        # ==========================================
        # Print a clear error message if the request fails
        # ==========================================
        print("Request failed.")
        print("Status code:", response.status_code)


# ==========================================
# Handle request-related errors such as
# connection problems or timeout problems
# ==========================================
except requests.exceptions.RequestException as e:
    print("Request failed.")
    print("Error:", e)


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
    