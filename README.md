# Latest News Program

This Python program gets the latest news headlines from the NewsAPI service and prints each headline title with its publication date.

## API Used

This project uses **NewsAPI.org**.

Endpoint used:
https://newsapi.org/v2/top-headlines

## Requirements

Make sure Python is installed on your computer.

You also need the `requests` library.

## Install Dependencies

Run this command in the terminal:

```bash
python -m pip install requests
```

## Get Your API Key

1. Go to https://newsapi.org/
2. Create an account or log in
3. Copy your API key from your dashboard

## Set Your API Key

This project uses an environment variable named `NEWS_API_KEY`.

### Mac / Linux

Run this in the terminal:

```bash
export NEWS_API_KEY="your_actual_api_key_here"
```

### Windows PowerShell

Run this in PowerShell:

```powershell
$env:NEWS_API_KEY="your_actual_api_key_here"
```

## Run the Program

In the terminal, run:

```bash
python latest_news.py
```

## What the Program Does

- Sends a GET request to the NewsAPI top headlines endpoint
- Checks if the request was successful
- Reads the JSON response
- Prints the headline title and publication date
- Prints the total number of headlines shown

## Error Handling

The program handles these common problems:

- Missing API key
- Request failure
- JSON parsing errors
- No articles returned

If the API key is missing, the program prints:

```text
API key not found. Please set your API key.
```

## Important Note

Do not upload your real API key to GitHub.

If you use a file like `config.py` for your key instead of an environment variable, add `config.py` to `.gitignore`.