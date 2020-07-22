from tkinter import *

root = Tk()

def clickFunction():
    label = Label(root, text = "this is tkinter buttons example")
    label.pack()

button1 = Button(root, text="click", command = clickFunction, fg = "white", bg = "Black")
button2 = Button(root, text="Next", state = DISABLED)
button3 = Button(root, text="Back", padx = 50, pady = 10)


button1.pack()
button2.pack()
button3.pack()



root.mainloop()
