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

print(dailydata.duplicated())

print(dailydata.duplicated(subset=["Volume"]))

print(dailydata.isnull())

print(dailydata.isna())

print(dailydata.isna().sum())

newdataform=pd.read_csv("AMZN new.csv")

print(newdataform)

latest_data=newdataform[newdataform["Date"] > "2020-09-23"]

print(latest_data)

df_row=pd.concat([dailydata, newdataform])

print(df_row)

df_row_reindex = pd.concat([dailydata, newdataform], ignore_index=True)

print(df_row_reindex)

print(df_row_reindex.sort_values("Date"))

print(df_row_reindex.drop_duplicates(subset=['Date']))

newdata_list=df_row_reindex.values.tolist()

print(newdata_list)

print(df_row_reindex[["Date", "Open"]])

data_wo_dup=df_row_reindex.drop_duplicates(subset=['Date'])

print(data_wo_dup)

date_and_open=data_wo_dup[["Date", "Open"]]

print(date_and_open)