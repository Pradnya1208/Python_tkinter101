from tkinter import *

root = Tk()



def clkFunc(value):
    label = Label(root, text = value)
    label.pack()

SHELF = [("Sapiens","Harari"),
    ("War and Peace","Tolstoy"),
    ("Ram","Amish")]

author = StringVar()
author.set("Harari")

for  bookname, auth in SHELF:
    Radiobutton(root, text = bookname, variable = author, value = auth).pack()


label = Label(root, text = author.get())
label.pack()


mybutton = Button(root, text ="click", command = lambda: clkFunc(author.get()))
mybutton.pack()
root.mainloop()
