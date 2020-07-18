# tkinter grid system is relative

from tkinter import *

root = Tk()
label1 = Label(root, text = "Hello world").grid(row = 0, column = 0)
label2 = Label(root, text = "This is tkinter grid example").grid(row = 1, column = 5)


root.mainloop()
