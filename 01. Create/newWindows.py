from tkinter import *


root = Tk()
lbl = Label(root, text= "Base Window").pack()

def opnWindow():
    top = Toplevel()
    label = Label(top, text = "New window").pack()
 

btn = Button(root, text = "Open", command = opnWindow).pack()



root.mainloop()
