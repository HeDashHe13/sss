import numpy as np
import pandas as pd
import ccxt
from VaderSentiment.vader Sentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv
import os
import transformers
API_KEY="6e14d133-9595-4b9f-85f4-9b67304163e3"
from dotenv import load_dotenv
import os
YOUR_COINBASE_PASSPHRASE = HeDashHe13!
YOUR_COINBASE_SECRET = N/A
load_dotenv()  # Load variables from .env into the environment

api_key = os.getenv("API_KEY")
print(f"My API Key is: {API_KEY}")
# ------------------ COINBASE PRO ------------------
exchange_class = getattr(ccxt, 'coinbasepro', ccxt.gdax)
    coinbase = exchange_class({
        'apiKey': COINBASE_API_KEY,
        'secret': COINBASE_SECRET,
        'password': COINBASE_PASSPHRASE,
        'enableRateLimit': True,
    })

    coinbase_balance = coinbase.fetch_balance()
    btc_price_coinbase = coinbase.fetch_ticker('BTC/USD')['last']
    print("\n✅ Coinbase Pro Connected")
    print("Balances:", coinbase_balance['total'])
    print("BTC Price (Coinbase Pro):", btc_price_coinbase)
except Exception as e:
    print("\n❌ Coinbase Pro Error:", type(e).__name__, str(e))
