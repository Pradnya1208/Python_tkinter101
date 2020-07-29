from guizero import *
from tkinter import *

app=App(title='Test',bg=(53, 60, 81))
root = app.tk

def hello():
    print ("hello!")


#creates menubar
menubar = Menu(root,relief=FLAT,bd=0)




# Sets menubar background color and active select but does not remove 3d  effect/padding
menubar.config(bg = "GREEN",fg='white',activebackground='red',activeforeground='pink',relief=FLAT)


# First item on menubar and creates sub options
filemenu = Menu(menubar, tearoff=0,relief=FLAT, font=("Verdana", 12),activebackground='red')
filemenu.config(bg = "GREEN")
filemenu.add_command(label="New (Ctrl + N)", command=hello)
filemenu.add_command(label="Save(Ctrl + S)", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)



# Adds to menubar and creates sub options
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0,bg='green',fg='blue')

helpmenu.add_command(label="Report bug", command=hello)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)

helpmenu.activebackground='red'



root.config(menu=menubar)
app.display()