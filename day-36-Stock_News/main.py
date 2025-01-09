import requests
import datetime as dt

from win32ctypes.pywin32.pywintypes import datetime

YESTERDAY = dt.datetime.now() - dt.timedelta(1)
PRE_YESTERDAY = YESTERDAY - dt.timedelta(1)

YESTERDAY_STR = str(YESTERDAY).split()[0]
PRE_YESTERDAY_STR = str(PRE_YESTERDAY).split()[0]


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = os.environ['ALPHA_API'] 
#RANGE = str(YESTERDAY).split()[0] + "&" + str(PRE_YESTERDAY).split()[0]


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": ALPHA_API_KEY,
}

alpha_url = "https://www.alphavantage.co/query"
request = requests.get(alpha_url, params=alpha_parameters)
data = request.json()


yesterday_close = float(data["Time Series (Daily)"][YESTERDAY_STR]["4. close"])
pre_yesterday_close = float(data["Time Series (Daily)"][PRE_YESTERDAY_STR]["4. close"])

difference = abs(yesterday_close - pre_yesterday_close)

if difference > 5:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    print("Get News")

    API_NEWS_KEY = os.environ['API_NEWS'] 

    news_parameters = {
        "q": COMPANY_NAME,
        "from": str(dt.datetime.today()).split()[0],
        #"sortBy": "popularity",
        "apiKey": API_NEWS_KEY,
    }

    news_url = ('https://newsapi.org/v2/everything')

    news_response = requests.get(news_url, params=news_parameters)
    news_data = news_response.json()
    print(news_data["articles"]["title"])
    print(news_data["articles"]["description"])
    print(news_data["articles"]["url"])





## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

