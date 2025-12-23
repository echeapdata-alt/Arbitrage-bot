import requests
import time

COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/markets"
VS_CURRENCY = "usd"
PER_PAGE = 250
MAX_RETRIES = 5
RETRY_DELAY = 5  # seconds

def get_prices():
    params = {
        "vs_currency": VS_CURRENCY,
        "order": "market_cap_desc",
        "per_page": PER_PAGE,
        "page": 1,
        "sparkline": "false"
    }

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"Fetching prices... Attempt {attempt}")
            response = requests.get(COINGECKO_URL, params=params, timeout=10)
            response.raise_for_status()  # raise exception for HTTP errors
            data = response.json()
            if not data:
                raise ValueError("Empty response from CoinGecko")
            prices = {coin["symbol"].upper(): coin["current_price"] for coin in data}
            return prices
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:
                print(f"Rate limit hit. Waiting {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
            else:
                print("HTTP error:", e)
                break
        except Exception as e:
            print("Error fetching prices:", e)
            time.sleep(RETRY_DELAY)
    return {}

def main():
    try:
        prices = get_prices()
        if prices:
            print("Fetched prices successfully!")
            # Show first 10 coins for testing
            for symbol, price in list(prices.items())[:10]:
                print(symbol, price)
        else:
            print("No prices fetched. Check API or network.")
    except Exception as e:
        print("Unexpected error in main:", e)

if __name__ == "__main__":
    print("Starting arbitrage bot...")
    main()
