import json
import time
import requests
import tradingview_ta


# functions for json file handle
def set_data(side):
    data = {"side": side}
    with open("data.json", "w") as outfile:
        json.dump(data, outfile)


def get_data():
    f = open("data.json")
    data = json.load(f)
    return data


def get_trades():
    f = open("trades.json")
    data = json.load(f)
    return data


def get_last_trade():
    a = get_trades()
    return a[list(a.keys())[-1]]


def set_last_trade(trade):
    a = get_trades()
    a[list(a.keys())[-1]] = trade
    with open("trades.json", "w") as outfile:
        json.dump(a, outfile)


def set_new_trade(trade):
    a = get_trades()
    a[int(list(a.keys())[-1]) + 1] = trade
    with open("trades.json", "w") as outfile:
        json.dump(a, outfile)


# --------------------------------


# functions for market data handle


def get_analysis():
    handler = tradingview_ta.TA_Handler(
        symbol="BTCUSDC",
        exchange="KRAKEN",
        screener="crypto",
        interval="1m",
        timeout=None,
    )
    analysis = handler.get_analysis()
    return analysis.summary


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


def get_diff():
    period1, period2 = 20, 50
    ema1 = get_ema(20, "1m")
    """ print(
        "EMA " + str(period1) + " " + str(ema1) + " at:",
        time.strftime("%Y-%m-%d %H:%M:%S"),
    ) """
    time.sleep(16)
    ema2 = get_ema(50, "1m")
    """ print(
        "EMA " + str(period2) + " " + str(ema2) + " at:",
        time.strftime("%Y-%m-%d %H:%M:%S"),
    ) """
    diff = ema1 - ema2
    print(
        "DIFF EMA "
        + str(period1)
        + " - EMA "
        + str(period2)
        + " = "
        + str(diff)
        + " at:",
        time.strftime("%Y-%m-%d %H:%M:%S"),
    )
    return diff


def get_btc_value():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USDT"
    response = requests.request("GET", url)
    return response.json()["USDT"]


# --------------------------------


def open_trade(side, startTime, btcValue):
    trade = {
        "side": side,
        "start time": startTime,
        "open value": btcValue,
    }
    set_new_trade(trade)


def close_trade(closeTime, btcValue):
    last_trade = get_last_trade()
    last_trade["close time"] = closeTime
    last_trade["close value"] = btcValue
    profit = (
        last_trade["open value"] - btcValue
        if last_trade["side"] == "sell"
        else btcValue - last_trade["open value"]
    )
    last_trade["profit"] = profit
    last_trade["profit perc"] = profit * 100 / btcValue
    set_last_trade(last_trade)
