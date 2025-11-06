import tkinter as tk
import tkinter.messagebox as tmsg


def dispLabel():
    lbl.configure(text="こんにちは")
    tmsg.showerror("info", "こんにちは")


root = tk.Tk()
root.geometry("200x200")

lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH", command=dispLabel)

lbl.pack()
btn.pack()

tk.mainloop()
