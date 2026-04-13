import pandas as pd

df = pd.read_csv("test.csv")

print("-------")
print(df.loc[2])
print("-------")
print(df.loc[[2]])
print("-------")
print(df.loc[[2, 3]])
print("-------")
print(df.loc[2]["国語"])

# 複数の行のデータを表示
print("-------loc")
print("index=", df.index.values)
print("slice 1-4 loc\n", df.loc[1:4])
print(type(df.loc[1:4]))

print("-------loc2")
df.index = ["0", "1", "2", "3", "4", "5"]
print("index=", df.index.values)
print("slice 1-4 loc\n", df.loc["1":"4"])

print("-------iloc")
print("slice 1-4 iloc\n", df.iloc[1:4])
