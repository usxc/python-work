import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# ソート（並べ替え）をして表示
kokugo = df.sort_values("国語", ascending=False)
print("国語の点数が高いもの順でソート\n", kokugo)
print("df = \n", df)

df.sort_values("国語", ascending=False, inplace=True)
print("df = \n", df)
