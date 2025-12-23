import requests

def get_prices():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 250,
        "page": 1,
        "sparkline": False
    }

    try:
        r = requests.get(url, params=params, timeout=15)
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        print("ERROR fetching data:", e)
        return {}

    prices = {}
    for item in data:
        prices[item["symbol"].upper() + "USD"] = float(item["current_price"])
    return prices


def main():
    print("Fetching prices...")
    prices = get_prices()

    if not prices:
        print("No prices fetched. Check API or network.")
        return

    # Show first 10 coins for testing
    count = 0
    for symbol, price in prices.items():
        print(symbol, price)
        count += 1
        if count == 10:
            break


if __name__ == "__main__":
    main()
