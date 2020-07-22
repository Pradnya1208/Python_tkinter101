from tkinter import *

root = Tk()

def show():
    label = Label(root, text = var.get()).pack()

var = StringVar()

check = Checkbutton(root , text="check", variable = var, onvalue = "on", offvalue = "off")
check.deselect()
check.pack()


btn = Button(root, text = "select" ,command =show).pack()

root.mainloop()
