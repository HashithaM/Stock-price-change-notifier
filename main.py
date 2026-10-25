import os
import smtplib

import requests


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def required_env(name):
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def main():
    stock_api_key = required_env("ALPHA_VANTAGE_API_KEY")
    news_api_key = required_env("NEWS_API_KEY")
    smtp_user = required_env("SMTP_USER")
    smtp_password = required_env("SMTP_PASSWORD")
    notification_recipient = required_env("NOTIFICATION_RECIPIENT")

    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "datatype": "json",
        "apikey": stock_api_key,
    }
    news_parameters = {
        "apiKey": news_api_key,
        "qInTitle": COMPANY_NAME,
    }

    response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters, timeout=30)
    response.raise_for_status()
    data_list = list(response.json()["Time Series (Daily)"].values())

    yesterday_closing_price = float(data_list[0]["4. close"])
    day_before_closing_price = float(data_list[1]["4. close"])
    difference = yesterday_closing_price - day_before_closing_price
    direction = "UP" if difference > 0 else "DOWN"
    diff_percent = round((difference / yesterday_closing_price) * 100)

    if abs(diff_percent) >= 0:
        news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters, timeout=30)
        news_response.raise_for_status()
        articles = news_response.json()["articles"][:3]
        formatted_articles = [
            f"{STOCK_NAME}: {direction} {diff_percent}%\n"
            f"Headline: {article['title']}\nBrief: {article['description']}"
            for article in articles
        ]

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=smtp_user, password=smtp_password)
            for article in formatted_articles:
                connection.sendmail(
                    from_addr=smtp_user,
                    to_addrs=notification_recipient,
                    msg=f"Subject: Stock price difference\n\n{article}",
                )


if __name__ == "__main__":
    main()
