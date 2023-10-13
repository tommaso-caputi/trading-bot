import schedule
import time
from utils import *


def main():
    global count
    if count == 7:
        count = 0
    count += 1

    analysis = get_analysis()
    data = get_last_trade()
    trade = [False, ""]
    if analysis["RECOMMENDATION"] == "BUY" and (
        data["side"] == "sell" or data["side"] == ""
    ):  # buy
        trade = [True, "buy"]
        print("buy")
    elif analysis["RECOMMENDATION"] == "SELL" and (
        data["side"] == "buy" or data["side"] == ""
    ):  # sell
        trade = [True, "sell"]
        print("sell")
    if trade[0] == True:
        nowTime = time.strftime("%Y-%m-%d %H:%M:%S")
        btcValue = get_btc_value()
        close_trade(nowTime, btcValue)
        open_trade(trade[1], nowTime, btcValue)
    print("--------------------------------------------------")


schedule.every(1).minutes.do(main)

count = 0
if __name__ == "__main__":
    main()
    while True:
        schedule.run_pending()
        time.sleep(1)


""" def main_ema_strategy():
    global count
    if count == 7:
        count = 0
    count += 1

    diff = get_diff()
    data = get_last_trade()
    trade = [False, ""]
    if diff > 0 and (data["side"] == "sell" or data["side"] == ""):  # buy
        trade = [True, "buy"]
        print("buy")
    elif diff < 0 and (data["side"] == "buy" or data["side"] == ""):  # sell
        trade = [True, "sell"]
        print("sell")
    if trade[0] == True:
        nowTime = time.strftime("%Y-%m-%d %H:%M:%S")
        btcValue = get_btc_value()
        close_trade(nowTime, btcValue)
        open_trade(trade[1], nowTime, btcValue)
    print("--------------------------------------------------") """
