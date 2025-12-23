import requests

def get_prices():
    url = "https://api.bybit.com/v5/market/tickers?category=spot"
    r = requests.get(url, timeout=15)

    # DEBUG: show status if something is wrong
    if r.status_code != 200:
        print("HTTP ERROR:", r.status_code)
        print(r.text)
        return {}

    try:
        data = r.json()
    except Exception as e:
        print("JSON ERROR:", e)
        print("RAW RESPONSE:")
        print(r.text)
        return {}

    prices = {}
    if "result" in data and "list" in data["result"]:
        for item in data["result"]["list"]:
            prices[item["symbol"]] = float(item["lastPrice"])

    return prices
