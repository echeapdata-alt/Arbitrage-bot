import requests
import time

BASE_AMOUNT = 100  # start with 100 USDT
THRESHOLD = 0.2    # % profit needed

def price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    return float(requests.get(url, timeout=10).json()["price"])

while True:
    try:
        btc_usdt = price("BTCUSDT")
        eth_btc  = price("ETHBTC")
        eth_usdt = price("ETHUSDT")

        btc = BASE_AMOUNT / btc_usdt
        eth = btc / eth_btc
        final_usdt = eth * eth_usdt

        profit = final_usdt - BASE_AMOUNT
        percent = (profit / BASE_AMOUNT) * 100

        print(f"\nStart: {BASE_AMOUNT} USDT")
        print(f"End:   {final_usdt:.4f} USDT")
        print(f"Profit: {profit:.4f} USDT ({percent:.3f}%)")

        if percent > THRESHOLD:
            print("🔥 TRIANGULAR ARBITRAGE OPPORTUNITY 🔥")

    except Exception as e:
        print("Error:", e)

    time.sleep(5)
