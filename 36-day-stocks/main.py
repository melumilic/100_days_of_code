from urllib import request
import requests
import os
import pandas as pd
import numpy as np

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
av_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "datatype": "csv",
    "outputsize": "compact",
    "apikey": ALPHA_VANTAGE_API_KEY,
}

# with open(os.path.split(av_url)[1]+".csv", 'wb') as f, \
#         requests.get(av_url,params=av_params, stream=True) as r:
#     for line in r.iter_lines():
#         f.write(line+'\n'.encode())

stock_df = pd.read_csv("query.csv", index_col="timestamp", parse_dates=True)
stock_df = stock_df.sort_values(by="timestamp", ascending=True)

stock_df["%change"] = np.where(
    True,
    (stock_df["close"] - stock_df["close"].shift(1)) / stock_df["close"].shift(1),
    0,
)
stock_df["change"] = np.where(
    np.abs(
        (stock_df["close"] - stock_df["close"].shift(1)) / stock_df["close"].shift(1)
    )
    >= 0.05,
    1,
    0,
)

print(stock_df.loc[stock_df["change"] == 1])
stock_df = stock_df.loc[::-1]
print(stock_df.iloc[0:50])
print(stock_df.tail())
if stock_df["change"][0] == 1:
    print("Get News")
print(stock_df.index[0].date())
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_PARAMS = {
    "apiKey": NEWS_API_KEY,
    "q": STOCK + " OR " + COMPANY_NAME,
    "to": stock_df.index[0].date(),
    "language": "en",
}
news_response = requests.get(NEWS_API_ENDPOINT, params=NEWS_API_PARAMS)
news_response.raise_for_status()
# print(news_response.json()["articles"])
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
