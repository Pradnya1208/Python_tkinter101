from tkinter import *

root = Tk()

e  = Entry(root, width = 35, borderwidth = 8)
e.grid(row = 0, column = 0, columnspan = 3, padx =10, pady=10)

global prev_sum
prev_sum =0


def add(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def clear():
    e.delete(0,END)

def addFunction():
    number_1 = e.get()    
    global first_num
    first_num = int(number_1)
    e.delete(0,END)
    

def equalFunction():
    
    number_2 = e.get()
    e.delete(0,END)
    e.insert(0, first_num + int(number_2))

  

    

button_1  = Button(root, text = "1", padx = 40, pady = 20, command = lambda: add(1))
button_2  = Button(root, text = "2", padx = 40, pady = 20, command = lambda: add(2))
button_3  = Button(root, text = "3", padx = 40, pady = 20, command = lambda: add(3))
button_4  = Button(root, text = "4", padx = 40, pady = 20, command = lambda: add(4))
button_5  = Button(root, text = "5", padx = 40, pady = 20, command = lambda: add(5))
button_6  = Button(root, text = "6", padx = 40, pady = 20, command = lambda: add(6))
button_7  = Button(root, text = "7", padx = 40, pady = 20, command = lambda: add(7))
button_8  = Button(root, text = "8", padx = 40, pady = 20, command = lambda: add(8))
button_9  = Button(root, text = "9", padx = 40, pady = 20, command = lambda: add(9))
button_0  = Button(root, text = "0", padx = 40, pady = 20, command = lambda: add(0))

button_add = Button(root, text = "+", padx = 40, pady = 20, command = addFunction)
button_eq = Button(root, text = "=", padx = 87, pady = 20, command = equalFunction)
button_clr = Button(root, text = "clear", padx = 78, pady = 20, command = clear)

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_0.grid(row = 4, column = 0)

button_add.grid(row = 5, column = 0)
button_eq.grid(row = 5, column = 1, columnspan =2)
button_clr.grid(row = 4, column = 1, columnspan =2)



root.mainloop()
