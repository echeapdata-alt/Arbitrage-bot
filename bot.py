import requests
import time

def get_prices():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 250,
        "page": 1,
        "sparkline": "false"
    }

    for attempt in range(5):
        try:
            r = requests.get(url, params=params, timeout=10)
            if r.status_code == 429:
                print("Rate limit hit. Waiting 10 seconds...")
                time.sleep(10)
                continue
            r.raise_for_status()
            data = r.json()
            prices = {coin['symbol'].upper(): coin['current_price'] for coin in data}
            return prices
        except Exception as e:
            print(f"Error fetching data: {e}")
            time.sleep(5)
    print("No prices fetched. Check API or network.")
    return {}
