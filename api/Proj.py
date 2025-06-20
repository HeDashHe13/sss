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
coinbase = ccxt.coinbasepro({
    'apiKey': 'YOUR_COINBASE_API_KEY',
    'secret': 'YOUR_COINBASE_SECRET ',
    'password': 'YOUR_COINBASE_PASSPHRASE',
    'enableRateLimit': True,
})

# Test Coinbase connection
try:
    balance = coinbase.fetch_balance()
    print("✅ Coinbase connected!")
    print("Balance:", balance['total'])
except Exception as e:
    print("❌ Coinbase error:", str(e))
