from tkinter import *
from PIL import ImageTk
import PIL.Image


IMAGE_PATH = 'a.png'
IMAGE = '..//back1.jpg'


root = Tk()
root.title("Icons and Images in tkinter")

imgicon = PhotoImage(file=IMAGE_PATH)
root.tk.call('wm', 'iconphoto', root._w, imgicon)


button = Button(root, text = "Exit", command= root.destroy).pack()

my_image = ImageTk.PhotoImage(PIL.Image.open(IMAGE))
label = Label(image = my_image).pack()


root.mainloop()
