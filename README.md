# Stock-price-change-notifier
This programme notify the stock price changes with the news using mails
This Python script retrieves stock data for a specific company (Tesla Inc in this case) from the Alpha Vantage API, compares the closing prices of the stock for two consecutive days, and sends an email containing recent news articles related to the company's stock.

Let's break down the script:

Import Statements:

requests: Used for making HTTP requests.
smtplib: Library for sending emails.
MIMEText: A module to create MIMEText objects representing email messages.
Constants:

STOCK_NAME: The symbol of the stock (e.g., "TSLA" for Tesla).
COMPANY_NAME: The name of the company.
STOCK_ENDPOINT: The URL for Alpha Vantage API.
NEWS_ENDPOINT: The URL for the News API.
NEWS_API_KEY: API key for the News API.
STOCK_API_KEY: API key for the Alpha Vantage API.
API Parameters:

stock_parameters: Parameters for querying stock data from the Alpha Vantage API.
news_parameters: Parameters for querying news articles related to the company from the News API.
Fetching Stock Data:

The script sends a GET request to the Alpha Vantage API to retrieve daily stock data for the specified company.
It extracts the closing prices for the last two days and calculates the price difference and percentage change.
Fetching News Articles:

It sends a GET request to the News API to fetch news articles related to the company.
The script retrieves the headlines and descriptions of the top three articles.
Formatting News Articles:

The script formats the retrieved articles into a readable format containing the stock symbol, price change percentage, headline, and brief description.
Sending Emails:

It configures an SMTP connection to Gmail and sends an email for each formatted news article to the specified recipient email address.
The email subject is "Stock price difference".
Comments and Print Statements:

The script contains commented out code related to MIMEText objects for email content formatting.
It also includes print statements for debugging purposes, displaying HTTP response codes and retrieved data.
Overall, this script demonstrates how to retrieve stock data, fetch related news articles, format the information, and send it via email using Python.






