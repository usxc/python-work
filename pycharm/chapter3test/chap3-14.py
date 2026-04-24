import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = [
    "Hiragino Maru Gothic Pro",
    "Hiragino Sans",
    "BIZ UDGothic",
    "MS Gothic"
]

df = pd.read_csv("test.csv")

df.plot()
plt.show()
