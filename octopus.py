import pandas as pd
import datetime

df = pd.read_csv('./octopus.csv')

# print(df.to_string()) 

# df['StartTime'] = pd.to_datetime(df['StartTime']).dt.date
df['StartTime'] = pd.to_datetime(df['StartTime'], format="%Y-%m-%dT%H:%M:%S")

print(df) 

# 2022-06-01T23:30:00+01:00