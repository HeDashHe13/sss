import os
import ccxt
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Assign variables (make sure to set them in your .env file)
COINBASE_API_KEY = os.getenv("COINBASE_API_KEY")
COINBASE_SECRET = os.getenv("COINBASE_SECRET")
COINBASE_PASSPHRASE = os.getenv("COINBASE_PASSPHRASE")

# Print for confirmation (optional)
print(f"My Coinbase API Key is: {COINBASE_API_KEY}")

# ------------------ COINBASE PRO ------------------
try:
    exchange_class = getattr(ccxt, 'coinbasepro', ccxt.gdax)
    coinbase = exchange_class({
        'apiKey': COINBASE_API_KEY,
        'secret': COINBASE_SECRET,
        'password': COINBASE_PASSPHRASE,
        'enableRateLimit': True,
    })

    # Retrieve account balance and BTC price
    coinbase_balance = coinbase.fetch_balance()
    btc_price_coinbase = coinbase.fetch_ticker('BTC/USD')['last']

    print("\n✅ Coinbase Pro Connected")
    print("Balances:", coinbase_balance['total'])
    print("BTC Price (Coinbase Pro):", btc_price_coinbase)

except Exception as e:
    print("\n❌ Coinbase Pro Error:", type(e).__name__, str(e))

