from tkinter import *


root = Tk()
root.geometry("400x400")

def slide():
    r = str(horz.get()) + "x" + str(vert.get())
    root.geometry(r)

vert = Scale(root, from_ = 0, to = 100)
vert.pack()

horz = Scale(root, from_ = 0, to = 100, orient = HORIZONTAL)
horz.pack()


btn= Button(root, text = "click", command = slide)
btn.pack()

root.mainloop()
