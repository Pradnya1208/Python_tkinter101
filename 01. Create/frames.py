from tkinter import *

root =  Tk()
root.geometry('650x500')


frame1 = Frame(root)
frame1.pack(fill=X)

lbl1 = Label(frame1, text="Title", width=6)
lbl1.pack(side=LEFT, padx=5, pady=5)

entry1 = Entry(frame1 )
entry1.pack(fill=X, padx=5, expand=True)

##############

frame2 = Frame(root)
frame2.pack(fill=BOTH)

#lbl2 = Label(frame2, text="Author", width=6)
#lbl2.pack(side=LEFT, padx=5, pady=5)

entry2 = Entry(frame2)
entry2.pack(fill=BOTH, padx=120,pady =50, expand=True)
########################################

frame3 = Frame(root)
frame3.pack( fill=BOTH)

#lbl3 = Label(frame3, text="Review", width=6)
#lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

entry3 = Entry(frame3)
entry3.pack(fill=BOTH, pady=50, padx=120, expand=True)

root.mainloop()
