from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql

db= mysql.connect(host="localhost",user="root",password="archi23",database="bookend")
cur = db.cursor()

allbookids =[]
def deleteBook():
    
    bid = bookInfo1.get()
    bid = int(bid)
    db= mysql.connect(host="localhost",user="root",password="archi23",database="bookend")
    cur = db.cursor()
    deleteSql = "delete from books where bid = {}".format(bid)
    try:
        bookidsSQL = "select bid from books"
        cur.execute(bookidsSQL)
        records = cur.fetchall()
        for i in records:
            allbookids.append(i[0])
        print(allbookids)
        if bid in allbookids:
            cur.execute(deleteSql)
            db.commit()
            messagebox.showinfo('Success',"Book Record Deleted Successfully")  
        else:
            messagebox.showinfo("ERROR","book id not found. CHECK THE ENTERED VALUE")
    except:
        messagebox.showinfo('ERROR',"Please check Book ID")
    allbookids.clear()

    print(bid)

    bookInfo1.delete(0, END)
    root.destroy()


def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,db,cur,root
    
    root = Tk()
    root.title("BOOK STORE MANAGEMENT SYSTEM")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
