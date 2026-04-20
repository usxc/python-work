import pandas as pd

df = pd.read_csv("test.csv")

data_e = df.query("数学 >= 70 and 英語 >= 70")
print("数学と英語が70点以上\n", data_e)

data_f = df.query("国語 > 英語")
print("英語より国語が得意な人 \n", data_f)

data_g = df.query("英語 % 2 == 0")
print("英語の点数が偶数 \n", data_g)
