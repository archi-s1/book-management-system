from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql


def bookRegister():
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    price= bookInfo3.get()
    quantity= bookInfo4.get()
    author = bookInfo5.get()
    pubID = bookInfo6.get()
    bid = int(bid)
    price = int(price)
    quantity = int(quantity)
    pubID = int(pubID)
    db = mysql.connect(host="localhost",user="root",password="archi23",database="bookend")
    cur = db.cursor()
    insertBooks = "insert into books(bid,title,price,quantity,author_pub,pubID) values({},'{}',{},{},'{}',{})".format(bid,title,price,quantity,author,pubID)
    try:
        cur.execute(insertBooks)
        db.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(bid)
    print(title)
    
    


    root.destroy()


def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,bookInfo5,bookInfo6,Canvas1,root
    
    root = Tk()
    root.title("BOOK STORE MANAGEMENT SYSTEM")
    root.minsize(width=500,height=500)
    root.geometry("700x600")
    
    db = mysql.connect(host="localhost",user="root",password="archi23",database="bookend")
    cur = db.cursor() 

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.1, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.1, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.25, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.25, relwidth=0.62, relheight=0.08)
        
    # Book price
    lb3 = Label(labelFrame,text="price : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.40, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.40, relwidth=0.62, relheight=0.08)
        
    # Book quantity
    lb4 = Label(labelFrame,text="quantity : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.55, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.55, relwidth=0.62, relheight=0.08)

    # Book author
    lb5 = Label(labelFrame,text="publication : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.70, relheight=0.08)
        
    bookInfo5 = Entry(labelFrame)
    bookInfo5.place(relx=0.3,rely=0.70, relwidth=0.62, relheight=0.08)

    # Book pubid
    lb6 = Label(labelFrame,text="publicationid : ", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.85, relheight=0.08)
        
    bookInfo6 = Entry(labelFrame)
    bookInfo6.place(relx=0.3,rely=0.85, relwidth=0.62, relheight=0.08)

    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.95, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.95, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
