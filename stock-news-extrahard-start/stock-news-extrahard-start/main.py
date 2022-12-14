import requests
from datetime import date

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
FUNC = "TIME_SERIES_INTRADAY"
TIME = "60min"

ALPHA_KEY = "AX5711Y1A98DLP87"
PARAM = {
    "function":FUNC,
    "symbol":STOCK,
    "interval":TIME,
    "apikey":ALPHA_KEY
}

date_t = date.today()

print(date_t.day)
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
r = requests.get("https://www.alphavantage.co/query", params=PARAM)
data = r.json()
print(data['Time Series (60min)'])
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

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

