import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# この１行を追加してください
df.index = ["0行目", "1行目", "2行目", "3行目", "4行目", "5行目"]  # ←これが重要

print("-------")
print(df.loc["2行目"])
print(type(df.loc["2行目"]))

print("-------")
print(df.loc[["2行目"]])

print("-------")
print(df.loc[["2行目", "3行目"]])

print("-------")
print(df.loc["2行目"]["国語"])
