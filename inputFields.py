from tkinter import *

root = Tk()

def clickFunc():
    label = Label(root, text = "Autor: " + entry1.get() + "->" + "Book : " + entry2.get())
    label.pack()


entry1 = Entry(root, width = 50, fg = "White", bg = "Black", borderwidth =10)
entry2 = Entry(root, width = 50, fg = "White", bg = "Black", borderwidth =10)
entry1.insert(0, "Enter Author Name")
entry2.insert(1, "Enter Book name")
entry1.pack()
entry2.pack()


button = Button(root, text = "Enter the author and book", command = clickFunc)
button.pack()

root.mainloop()
