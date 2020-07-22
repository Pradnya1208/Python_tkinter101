from tkinter import *
from tkinter import messagebox

root = Tk()
def popup1():
    messagebox.showinfo("messag box", "Hello world!")

def popup2():
    messagebox.showwarning("messag box", "Hello world!")

def popup3():
    messagebox.showerror("messag box", "Hello world!")

def popup4():
    messagebox.askokcancel("messag box", "Hello world!")

def popup5():
     response = messagebox.askquestion("messag box", "Hello world!")
     if response == "yes":
         Label(root, text = "Welcome").pack()
     else:
         Label(root, text = "Go back to menu").pack()

def popup6():
    messagebox.askyesno("messag box", "Hello world!")
         

Button(root, text = "info", command = popup1).pack()
Button(root, text = "warning", command = popup2).pack()
Button(root, text = "error", command = popup3).pack()
Button(root, text = "okcancel", command = popup4).pack()
Button(root, text = "ask question", command = popup5).pack()
Button(root, text = "ask yesno", command = popup6).pack()



root.mainloop()
