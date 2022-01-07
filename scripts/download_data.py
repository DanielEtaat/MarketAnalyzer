import os
import pandas as pd
import yfinance as yf
from datetime import datetime


def download(symb, interval):
    downloaded = [fname[:-4] for fname in os.listdir("data") if fname[-4:] == ".pkl"]
    for fname in downloaded:
        _symb, _interval = fname.split("_")
        if symb == _symb and interval == _interval:
            data = pd.read_pickle(f"data/{symb}_{interval}.pkl")
            stop = data.iloc[-1].name.date()
            if (datetime.now().date() - stop).days == 0:
                data = pd.concat([data, yf.download(symb, start=stop, interval=interval)])
            break
    else:
        print("Downloading...")
        data = yf.download(symb, period="max", interval=interval)
    data = data.dropna()
    data.to_pickle(f"data/{symb}_{interval}.pkl")
    return data