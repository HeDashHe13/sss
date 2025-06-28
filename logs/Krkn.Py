import ccxt

# Replace with your Kraken API credentials
api_key = 'My_key'
api_secret = 'My_secret'

kraken = ccxt.kraken({
    'apiKey': api_key,
    'secret': api_secret,
})

symbols = ['BTC/USD', 'ETH/USD', 'SOL/USD']  # Popular trading pairs on Kraken

def fetch_balances_and_prices(exchange):
    try:
        exchange.load_markets()
        
        # Fetch balances
        balance = exchange.fetch_balance()
        print("Kraken Account Balances:")
        non_zero = False
        for asset, amount in balance['total'].items():
            if amount > 0:
                print(f"  {asset}: {amount}")
                non_zero = True
        if not non_zero:
            print("  All balances are zero.")
        
        # Fetch live prices
        print("\nKraken Live Market Prices:")
        for symbol in symbols:
            if symbol in exchange.markets:
                ticker = exchange.fetch_ticker(symbol)
                print(f"  {symbol} → Last: {ticker['last']}, Bid: {ticker['bid']}, Ask: {ticker['ask']}")
            else:
                print(f"  Symbol {symbol} not available on Kraken.")
    except Exception as e:
        print(f"Error: {e}")

fetch_balances_and_prices(kraken)
