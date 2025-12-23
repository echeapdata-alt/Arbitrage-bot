import requests

url = "https://api.binance.com/api/v3/ticker/price"
prices = requests.get(url).json()

for coin in prices[:10]:  # just showing first 10 coins for testing
    print(coin["symbol"], coin["price"])