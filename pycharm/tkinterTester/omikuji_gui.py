import tkinter as tk
import random

KUJI = ["大吉", "中吉", "小吉", "凶"]

def draw():
    label.config(text=random.choice(KUJI))

root = tk.Tk()
root.geometry('230x150')
root.title('おみくじ')

label = tk.Label(root, text="—")
label.pack()
tk.Button(root, text="ひく", command=draw).pack()
root.mainloop()