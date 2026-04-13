import pandas as pd

df = pd.read_csv('test.csv')

print("-------")
print(df["国語"])
print(type(df["国語"]))
print("-------")
print(df[["国語"]])
print(type(df[["国語"]]))
print("-------")
print(df[["国語"]])
print(type(df[["国語"]]))
