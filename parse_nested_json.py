## Asiwome Agbleze
## CMSC 111/1
## Asignment 4:Parsing Nested JSON

# ==========================================
# Import the json module so the program
# can read JSON data from a file
# ==========================================
import json


# ==========================================
# Use a try-except block so the program
# can handle missing files or missing data
# without crashing
# ==========================================
try:

    # ==========================================
    # Open the JSON file and load the data
    # into a Python dictionary
    # ==========================================
    with open("nested_data.json", "r") as file:
        data = json.load(file)

    # ==========================================
    # Extract the required values from the
    # nested JSON structure
    # ==========================================
    student_name = data["student"]["name"]
    student_email = data["student"]["contact"]["email"]
    student_city = data["student"]["address"]["city"]
    first_course = data["student"]["courses"][0]["course_name"]
    second_course_grade = data["student"]["courses"][1]["grade"]

    # ==========================================
    # Print the required values
    # ==========================================
    print("Student Name:", student_name)
    print("Email:", student_email)
    print("City:", student_city)
    print("First Course:", first_course)
    print("Second Course Grade:", second_course_grade)


# ==========================================
# Handle missing keys, missing list items,
# missing file, or invalid JSON format
# Print the exact required message
# ==========================================
except (KeyError, IndexError, FileNotFoundError, json.JSONDecodeError):
    print("Missing data in JSON file.")