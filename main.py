import numpy as np

import pandas as pd

import requests

data=requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=AMZN&apikey=NPSUYHEF4CQO62UT")

api_data=data.json()

print(type(api_data))

print(api_data)

dailydata=pd.read_csv("AMZN.csv")

print(dailydata)

print(type("dailydata"))

dailydata.head()

dailydata.info()

dailydata.sort_values("Volume")

print(dailydata.columns)

print(dailydata.sort_values("Volume"))

print(dailydata.sort_values("Volume" , ascending=False))
