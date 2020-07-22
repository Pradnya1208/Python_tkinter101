from tkinter import *

root =  Tk()


frame = LabelFrame(root, text = "tkinter Frame", padx = 10, pady = 10, bg = "Red")
frame.pack(padx = 200, pady = 200)
button = Button(frame, text = "Frame Button", fg = "White", bg = "Black")
button.pack()


frame1 = LabelFrame(root, text = "tkinter Frame", padx = 10, pady = 10, bg = "Red")
frame1.pack(padx = 50, pady = 50)
button1 = Button(frame1, text = "Frame Button", fg = "White", bg = "Black")
button1.pack()

root.mainloop()
