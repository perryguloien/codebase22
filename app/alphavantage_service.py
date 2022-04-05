
# maybe something like the following rough organizational structure would be reasonable.
# then we can import these functions into other files that need them (i.e. crypto.py, stocks.py, unemployment.py).
# one benefit of doing so is we get to refactor all the request-related code out of those files.
# for example, as a result, we'll only have the api key definition in one place (which is good)!

import os
from dotenv import load_dotenv
from app.utils import to_usd
import requests
import json

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

def fetch_crypto_data(symbol):
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&market=USD&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    #print(parsed_response)
    #breakpoint()
    
    return parsed_response["Time Series (Digital Currency Daily)"]


def fetch_stocks_data(symbol):
    # url = ...
    # make a request
    # return some data
    return "TODO"


def fetch_unemployment_data():
    # url = ...
    # make a request
    # return some data
    return "TODO"
