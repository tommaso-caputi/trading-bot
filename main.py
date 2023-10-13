import schedule
import time
import requests
import json


def get_ema(period, interval):
    url = (
        "https://api.taapi.io/ema?secret=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjI0MWY4MGI0MjI0NmNlM2IwMWU3MjdiIiwiaWF0IjoxNjk3MTk0Mzk4LCJleHAiOjMzMjAxNjU4Mzk4fQ.MCTy5eLpNQgEq3goFSwmWgUTgdYUWdx6hBctL-yPtaA&exchange=binance&symbol=BTC/USDT&backtrack=1&interval="
        + interval
        + "&period="
        + str(period)
        + ""
    )
    response = requests.request("GET", url)
    response = response.json()
    return response["value"]


def main():
    period1, period2 = 20, 50
    ema1 = get_ema(20, "1m")
    print(
        "EMA " + str(period1) + " " + str(ema1) + " at:",
        time.strftime("%Y-%m-%d %H:%M:%S"),
    )
    time.sleep(16)
    ema2 = get_ema(50, "1m")
    print(
        "EMA " + str(period2) + " " + str(ema2) + " at:",
        time.strftime("%Y-%m-%d %H:%M:%S"),
    )
    print("--------------------------------------------------")


schedule.every(1).minutes.do(main)

main()
while True:
    schedule.run_pending()
    time.sleep(1)
