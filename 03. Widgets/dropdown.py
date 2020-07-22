from tkinter import *

root = Tk()

clicked = StringVar()
clicked.set("Country")

def show():
    lb = Label(root, text = clicked.get()).pack()


country = ["USA", "Brazil", "India", "Russia", "China", "France", "Germany","UK"]

drop = OptionMenu(root, clicked, *country)
drop.pack()

btn = Button(root, text = "show selection", command = show).pack()

root.mainloop()
