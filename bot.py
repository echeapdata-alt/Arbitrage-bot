import requests
import time

BASE_AMOUNT = 100
THRESHOLD = 0.2

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_price(symbol):
    url = "https://api.binance.com/api/v3/ticker/price"
    try:
        r = requests.get(url, params={"symbol": symbol}, headers=HEADERS, timeout=10)

        if r.status_code != 200:
            print(f"HTTP error {r.status_code} for {symbol}")
            return None

        data = r.json()

        if "price" not in data:
            print(f"Invalid response for {symbol}: {data}")
            return None

        return float(data["price"])

    except Exception as e:
        print(f"Request error for {symbol}: {e}")
        return None


while True:
    print("\nFetching prices...")

    btc_usdt = get_price("BTCUSDT")
    eth_btc  = get_price("ETHBTC")
    eth_usdt = get_price("ETHUSDT")

    if None in (btc_usdt, eth_btc, eth_usdt):
        print("Price fetch failed, retrying...")
        time.sleep(5)
        continue

    btc = BASE_AMOUNT / btc_usdt
    eth = btc / eth_btc
    final_usdt = eth * eth_usdt

    profit = final_usdt - BASE_AMOUNT
    percent = (profit / BASE_AMOUNT) * 100

    print(f"Start: {BASE_AMOUNT} USDT")
    print(f"End:   {final_usdt:.4f} USDT")
    print(f"Profit: {profit:.4f} USDT ({percent:.3f}%)")

    if percent > THRESHOLD:
        print("🔥 TRIANGULAR ARBITRAGE OPPORTUNITY 🔥")

    time.sleep(8)
