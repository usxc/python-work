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
