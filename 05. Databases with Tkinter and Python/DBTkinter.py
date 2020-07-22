from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import ImageTk
import PIL.Image
IMAGE = 'img.png'


#submit function
def submit():
    conn = sqlite3.connect("book_db1")
    c = conn.cursor()
    #insert into table
    c.execute("INSERT INTO book_data1 VALUES(:bookname, :author, :genre, :price)",
            {'bookname' : bookname.get(),
             'author': author.get(),
             'genre' : genre.get(),
             'price': price.get()
             })
    
    conn.commit()
    conn.close()
    bookname.delete(0, END)
    author.delete(0, END)
    genre.delete(0, END)
    price.delete(0, END)


# create query function
def show_query():
    conn = sqlite3.connect("book_db1")
    c = conn.cursor()
    c.execute("SELECT *, oid FROM book_data1")
    record   = c.fetchall()

    format_data(record)
    
    conn.commit()
    conn.close()


def format_data(record):
    book_data = ''
    auth_data = ''
    genre_data = ''
    price_data = ''
    id_num = ''
    column_names = ["Id", "Book", "Author", "Genre", "Price"]
    
    for rec in record:
        book_data += str(rec[0]) + "\n"
        auth_data += str(rec[1]) + "\n"
        genre_data += str(rec[2]) + "\n"
        price_data += str(rec[3]) + "\n"
        id_num += str(rec[4]) + "\n"
        
    display_records(book_data,auth_data,genre_data, price_data,column_names,id_num)



def display_records(book_data, auth_data, genre_data, price_data, column_names, id_num):
    top = Toplevel()
    top.title("Book Shelf")
    top.tk.call('wm', 'iconphoto', top._w, imgicon)
    
    label0 = Label(top, text = column_names[0] + "\n" + id_num)
    label0.grid(row= 0, column = 0)
    label1 = Label(top, text = column_names[1] + "\n" + book_data)
    label1.grid(row= 0, column = 1)
    label2 = Label(top, text = column_names[2] + "\n" + auth_data)
    label2.grid(row= 0, column = 2)
    label3 = Label(top, text = column_names[3] + "\n" + genre_data)
    label3.grid(row= 0, column = 3)
    label4 = Label(top, text = column_names[4] + "\n" + price_data)
    label4.grid(row= 0, column = 4)    

#create function to delete
def delete_query():
    if delete_box.get():   
        conn = sqlite3.connect("book_db1")
        c = conn.cursor()
        c.execute("DELETE from book_data1 WHERE oid = " + delete_box.get())
        record   = c.fetchall()
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Error", "Select ID first")


#create edit function to update
def edit_query():
    
    record_id = delete_box.get()
    if record_id:    
        conn = sqlite3.connect("book_db1")
        c = conn.cursor()
        c.execute("SELECT * FROM book_data1 WHERE oid = " + str(record_id))
        record   = c.fetchall()
        if record:
            global editor
            editor = Toplevel()
            editor.title("Update Book Shelf")
            imgico = PhotoImage(file='edit.png') 
            editor.tk.call('wm', 'iconphoto', editor._w, imgico)
            create_entrypoints(editor)
            #Create save Buttons
            submit_btn = Button(editor, text = "Save Record", command = update)
            submit_btn.grid(row = 5, column =0, columnspan  = 2, pady = 8, padx = 8, ipadx = 80)
  
            for rec in record:
                bookname.insert(0, rec[0])
                author.insert(0, rec[1])
                genre.insert(0, rec[2])
                price.insert(0, rec[3])
        else:
            messagebox.showerror("Error", "Invalid ID" + "\n" + "Check the records first")
        conn.commit()
        conn.close()
    else:
       messagebox.showerror("Error", "Select ID first") 
   

def update():
    conn = sqlite3.connect("book_db1")
    c = conn.cursor()
    rec_id = delete_box.get()
    c.execute("""UPDATE book_data1 SET
        book_name = :book,
        author_name = :author,
        genre = :genre,
        price = :price
        
        WHERE oid = :oid""",
        {
         'book': bookname.get(),
         'author': author.get(),
         'genre' : genre.get(),
         'price': price.get(),
         'oid' : rec_id
        })


    conn.commit()
    conn.close()
    editor.destroy()



#Create entrypoint window
def create_entrypoints(root):
    global bookname, author, genre, price
    #create text boxes
    bookname = Entry(root, width = 30)
    bookname.grid (row = 0, column = 1, padx =20)

    author = Entry(root, width = 30)
    author.grid (row = 1, column = 1, padx =20)

    genre = Entry(root, width = 30)
    genre.grid (row = 2, column = 1, padx =20)

    price = Entry(root, width = 30)
    price.grid (row = 3, column = 1, padx =20)


    #Textbox labels
    bookname_lbl = Label(root, text = "Book Name")
    bookname_lbl.grid(row = 0, column = 0)

    author_lbl = Label(root, text = "Author Name")
    author_lbl.grid(row = 1, column = 0)

    genre_lbl = Label(root, text = "Genre")
    genre_lbl.grid(row = 2, column = 0)

    price_lbl = Label(root, text = "Price")
    price_lbl.grid(row = 3, column = 0)


  

    

def create_options(root):

    
    #Create submit Buttons
    submit_btn = Button(root, text = "Add Records", command = submit)
    submit_btn.grid(row = 5, column =0, columnspan  = 2, pady = 8, padx = 8, ipadx = 80)
   
    #create show data button
    query_btn = Button(root, text = "Show Records", command = show_query)
    query_btn.grid(row = 6, column = 0 , columnspan =2, pady =8, padx =8, ipadx = 120)

     
    
  

def select_opts(root):
    global delete_box
    #create select ID option
    delete_box_lbl = Label(root, text = "Select ID")
    delete_box_lbl.grid(row = 7, column = 0)
    delete_box = Entry(root, width = 30)
    delete_box.grid(row = 7, column = 1)
    create_options(root)
        
    #create delete button
    delete_btn = Button(root, text = "Delete Records", command = delete_query)
    delete_btn.grid(row = 8, column = 0 , columnspan =1, pady =8, padx = 60)

    #create update button
    update_btn = Button(root, text = "Update Records", command = edit_query)
    update_btn.grid(row = 8, column = 1 , columnspan =1, pady =8, padx =8)


def main():
    
    root = Tk()
    root.title("Book Shelf Entries")
    global imgicon
    imgicon = PhotoImage(file=IMAGE)   
    root.tk.call('wm', 'iconphoto', root._w, imgicon)
    create_entrypoints(root)
    create_options(root)
    select_opts(root)

    
    #create connection
    conn = sqlite3.connect("book_db1")

    #create Cursor
    c = conn.cursor()

    #create table
    c.execute("""CREATE TABLE IF NOT EXISTS book_data1(
            book_name text,
            author_name text,
            genre text,
            price integer
            )""")

    #commit Changes
    conn.commit()

    #close connection
    conn.close()

    root.mainloop()


if __name__ == "__main__":
    main()
