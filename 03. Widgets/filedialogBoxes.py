from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
import PIL.Image

root = Tk()


def selectFiles():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir = "img_text", title = "select a file", filetypes = (("jpg files", "*.jpg"),("txt files", "*.txt"),("all files", "*.*")))
    my_label = Label(root, text = root.filename).pack()
    my_image = ImageTk.PhotoImage(PIL.Image.open(root.filename))
    label = Label(image = my_image)
    label.pack()
    
    
btn = Button(root, text = "select files", command = selectFiles).pack()


root.mainloop()
