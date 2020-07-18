from  tkinter import *
from PIL import ImageTk
import PIL.Image


IMAGE_PATH = 'a.png'
IMAGE_PATH1 = '1.jpg'
IMAGE_PATH2 = '2.jpg'
IMAGE_PATH3 = '3.jpg'
IMAGE_PATH4 = '4.jpg'
IMAGE_PATH5 = '5.jpg'
IMAGE_PATH6 = '6.jpg'

root = Tk()
root.title("Icons and Images in tkinter")

imgicon = PhotoImage(file=IMAGE_PATH)
root.tk.call('wm', 'iconphoto', root._w, imgicon)



my_image1 = ImageTk.PhotoImage(PIL.Image.open(IMAGE_PATH1))
my_image2 = ImageTk.PhotoImage(PIL.Image.open(IMAGE_PATH2))
my_image3 = ImageTk.PhotoImage(PIL.Image.open(IMAGE_PATH3))
my_image4 = ImageTk.PhotoImage(PIL.Image.open(IMAGE_PATH4))
my_image5 = ImageTk.PhotoImage(PIL.Image.open(IMAGE_PATH5))
my_image6 = ImageTk.PhotoImage(PIL.Image.open(IMAGE_PATH6))

img_list = [my_image1, my_image2, my_image3, my_image4, my_image5, my_image6]
status = Label(root, text = "Image 1 of " + str(len(img_list)), bd =1, relief = SUNKEN)

label = Label(image = my_image1)
label.grid(row = 0 , column = 0, columnspan = 3)

def forward(img_number):
    global label
    global button_forward
    global button_back
    label.grid_forget()
    
    label = Label(image = img_list[img_number - 1])
    button_forward = Button(root, text = ">>", command  = lambda:forward(img_number + 1))
    button_back = Button(root, text = "<<" , command = lambda:backward(img_number - 1))

    if (img_number == len(img_list)):
        button_forward = Button(root, text = ">>", state = DISABLED)
         

    
    label.grid(row = 0 , column = 0, columnspan = 3)
    button_forward.grid(row = 1, column = 2)
    button_back.grid(row =1,column = 0 )

def backward(img_number):
    global label
    global button_forward
    global button_back
    label.grid_forget()

    label = Label(image = img_list[img_number - 1])
    button_forward = Button(root, text = ">>", command  = lambda:forward(img_number + 1))
    button_back = Button(root, text = "<<" , command = lambda:backward(img_number - 1))

    if (img_number == 1):
        button_back = Button(root, text = "<<", state = DISABLED)
         

    
    label.grid(row = 0 , column = 0, columnspan = 3)
    button_forward.grid(row = 1, column = 2)
    button_back.grid(row =1,column = 0 )

    


button_back = Button(root, text = "<<" , command = lambda:backward(2))
button_back.grid(row =1,column = 0 )
button_exit = Button(root, text = "Exit", command= root.destroy)
button_exit.grid(row =1, column =1)
button_forward = Button(root, text = ">>", command  = lambda:forward(2))
button_forward.grid(row = 1, column = 2, pady = 10)
status.grid(row =2, column =0, columnspan =3, sticky = W+E)

root.mainloop()
