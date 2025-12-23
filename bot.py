import requests
import time

def get_prices(retries=3, delay=5):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 250,
        "page": 1,
        "sparkline": False
    }

    for attempt in range(retries):
        try:
            r = requests.get(url, params=params, timeout=15)
            r.raise_for_status()
            data = r.json()
            prices = {item["symbol"].upper() + "USD": float(item["current_price"]) for item in data}
            return prices
        except requests.exceptions.HTTPError as e:
            if r.status_code == 429:
                print(f"Rate limited by CoinGecko. Waiting {delay}s before retry {attempt+1}/{retries}...")
                time.sleep(delay)
            else:
                print("HTTP error:", e)
                break
        except Exception as e:
            print("Other error:", e)
            break
    return {}
