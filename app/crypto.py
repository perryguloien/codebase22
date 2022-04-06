


print("CRYPTO REPORT...")

import os
import json
from app.alphavantage_service import fetch_crypto_data
from dotenv import load_dotenv
import requests
from app.utils import to_usd

load_dotenv()

#ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

symbol = input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"


tsd = fetch_crypto_data(symbol)
dates = list(tsd.keys())
latest_date = dates[0]
latest = tsd[latest_date]
#print(latest)
# not sure about the difference between '4a. close (USD)' and '4b. close (USD)'

print(symbol)
print(latest_date)
print(to_usd((float(latest['4a. close (USD)']))))

