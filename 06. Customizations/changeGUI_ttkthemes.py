from ttkthemes import ThemedStyle
import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title('App')

style = ThemedStyle(app)
style.set_theme("vista")

tktext = tk.Label(app, text=" tk Label")
tktext.pack()
tkbutton = tk.Button(app, text="tk Button")
tkbutton.pack()

text = ttk.Label(app, text=" ttk Label")
text.pack()
button = ttk.Button(app, text="ttk Button")
button.pack()

app.geometry('200x200')

app.mainloop()