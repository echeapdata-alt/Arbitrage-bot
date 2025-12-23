import requests

def get_prices():
    url = "https://api.bybit.com/v5/market/tickers?category=spot"
    r = requests.get(url, timeout=10)
    data = r.json()

    prices = {}
    for item in data["result"]["list"]:
        prices[item["symbol"]] = float(item["lastPrice"])

    return prices


def main():
    print("Fetching prices...")
    prices = get_prices()

    count = 0
    for symbol, price in prices.items():
        print(symbol, price)
        count += 1
        if count == 10:
            break


if __name__ == "__main__":
    main()
