import requests
import smtplib
from email.mime.text import MIMEText

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "6adf5849ff3047faaf64421280929ece"
STOCK_API_KEY = "RG5MNAJRDH7ESBOA"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "datatype": "json",
    "apikey": STOCK_API_KEY,
}
news_parameters = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
}


# STEP 1: Use https://www.alphavantage.co/documentation/#daily

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
print(response.status_code)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
print(data_list)
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]


day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = (float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference > 0:
    up_down = "UP "
else:
    up_down = "DOWN "

diff_percent = round((difference / float(yesterday_closing_price)) * 100)

if abs(diff_percent) >= 0:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    print(news_response.status_code)
    articles = news_response.json()["articles"]

# STEP 2: https://newsapi.org/

    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}% \nHeadline: {article['title']}. \n Brief: {article['description']}" for article in three_articles]
    print(formatted_articles)

# STEP 3: Use twilio.com/docs/sms/quickstart/python
    my_email = "pythontesting0032@gmail.com"
    password = ""

    for article in formatted_articles:
        # article = MIMEText(article, 'plain', 'utf-8')
        print(article)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="kanthiwijesinghe71@gmail.com",
                                msg=f"subject:Stock price difference\n\n{article}")
            connection.close()

