import json


def get_ema_from_file(name):
    f = open("" + name + ".json")
    data = json.load(f)
    b = []
    for a in data:
        b.append(a["value"])
    return b


def set_data(side, diff):
    data = {"side": side, "diff": diff}
    with open("data.json", "w") as outfile:
        json.dump(data, outfile)


def get_data():
    f = open("data.json")
    data = json.load(f)
    return data


a = get_ema_from_file("20")
b = get_ema_from_file("50")

diffs = []
for i in range(len(a)):
    diff = a[i] - b[i]
    diffs.append(a[i] - b[i])

    data = get_data()
    if diff > 0 and (data["side"] == "sell" or data["side"] == ""):  # buy
        print("buy")
        set_data("buy", diff)
    elif diff < 0 and (data["side"] == "buy" or data["side"] == ""):  # sell
        print("sell")
        set_data("sell", diff)


print(diffs)
