import ccxt

# Replace with your Kraken API credentials
api_key = 'w3Lb6ULZN7TlQEnjTi8Oyf/Sp+562PAsQeSgqt92FTp7BsfyednOccMv'
api_secret = '3B3k8iVrF9jQDbIombuSoJlGEg48bpJlzi0esHpOOnaxRzv5pDc6hte7d337Qhpna/qHVkD8kaKbBv8tO0HKDA=='

kraken = ccxt.kraken({
    'apiKey': api_key,
    'secret': api_secret,
})

try:
    kraken.load_markets()

    # ✅ Fetch account balances
    balance = kraken.fetch_balance()
    print("📊 Account Balances:")
    for asset, amount in balance['total'].items():
        if amount > 0:
            print(f"  {asset}: {amount}")
    if not any(balance['total'].values()):
        print("  (No funds available)")

    # ✅ Fetch live market prices
    print("\n💱 Live Market Prices:")
    symbols = ['BTC/USD', 'ETH/USD']
    for symbol in symbols:
        ticker = kraken.fetch_ticker(symbol)
        print(f"  {symbol} → Last: {ticker['last']} | Bid: {ticker['bid']} | Ask: {ticker['ask']}")

    # 🧪 Simulated Market Buy Order
    buy_order = {
        'symbol': 'BTC/USD',
        'side': 'buy',
        'type': 'market',
        'amount': 0.001
    }

    # 🧪 Simulated Market Sell Order
    sell_order = {
        'symbol': 'BTC/USD',
        'side': 'sell',
        'type': 'market',
        'amount': 0.001
    }

    print("\n🧪 Simulated Orders (No actual trades):")
    print(f"  BUY  → {buy_order['amount']} {buy_order['symbol']} at market price")
    print(f"  SELL → {sell_order['amount']} {sell_order['symbol']} at market price")
    print("  ✅ This is a simulation. No orders were placed.")

except ccxt.AuthenticationError:
    print("❌ Authentication failed. Check your Kraken API key and secret.")
except ccxt.NetworkError as e:
    print(f"🌐 Network error: {e}")
except Exception as e:
    print(f"⚠️ Error: {e}")
