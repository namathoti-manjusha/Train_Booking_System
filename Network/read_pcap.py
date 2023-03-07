import pandas as pd
df=pd.read_csv("captured_packets.csv")
print(df.columns)
print(df.groupby('Protocol').sum())
print(df)