from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql

db=mysql.connect(host="localhost",user="root",password="archi23",database="bookend")
cur = db.cursor()


allBid = []
allBillID = []

def sales():

    global SubmitBtn,labelFrame,root,Canvas1,status,bookInfo1,bookInfo2,bookInfo3,bookInfo4,bookInfo5,bookInfo6,lb1,quitBtn
    BillID= bookInfo1.get()
    nme = bookInfo2.get()
    bsold = bookInfo3.get()
    saledt = bookInfo4.get()
    price = bookInfo5.get()
    qty = bookInfo6.get()
    BillID = int(BillID)
    bsold = int(bsold)
    price = int(price)
    qty = int(qty)
    

    SubmitBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    bookInfo1.destroy()
    bookInfo2.destroy()
    bookInfo3.destroy()
    bookInfo4.destroy()
    bookInfo5.destroy()
    bookInfo6.destroy()
    
    db=mysql.connect(host="localhost",user="root",password="archi23",database="bookend")
    cur = db.cursor()

    extractbillID = "select BillID from sales"
    extractBID = "select bid from books"
    #try:
    cur.execute(extractbillID)
    rec=cur.fetchall()
    cur.execute(extractBID)
    abc = cur.fetchall()
    for i in abc:
        allBid.append(i[0])

    for j in rec:
        allBillID.append(j[0])

    try:
        if BillID in allBillID:
            messagebox.showifo("Error","CHECK BillID")
            status = True
        elif bsold not in allBid:
            messagebox.showinfo("error","NO records found for the given book ID")
            status = True
        else:
            status = False

    except:
        messagebox.showinfo("Error","Can't fetch BillIDS")

    salesSql= "insert into sales(BillID,custname,bidsold,saledt,price,qty) values({},'{}',{},'{}',{},{})".format(BillID,nme,bsold,saledt,price,qty)
    try:
        if status== False:
            cur.execute(salesSql)
            db.commit()
            messagebox.showinfo('Success',"Sales record updated successfully")
            root.destroy()

        else:
            messagebox.showinfo('Message',"Bill ID already exists.")
            root.destroy()
            
        allBillID.clear()
        allBid.clear()
    except:
        messagebox.showinfo("Search Error","The values entered are wrong, TRY AGAIN")

    print(BillID)
    print(nme)
    print(bsold)
    print(saledt)

            
def salesadd(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,bookInfo5,bookInfo6,Canvas1,db,cur,root,lb1,labelFrame,SubmitBtn,quitBtn,status
    
    root = Tk()
    root.title("BOOK STORE MANAGEMENT SYSTEM")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    db = mysql.connect(host="localhost",user="root",password="archi23",database="bookend")
    cur = db.cursor()

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Sales record", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    
    lb1 = Label(labelFrame,text="Bill ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.1, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.1, relwidth=0.62, relheight=0.08)
        
    
    lb2 = Label(labelFrame,text="Customer name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.25, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.25, relwidth=0.62, relheight=0.08)
        
    
    lb3 = Label(labelFrame,text="Book id purchased : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.40, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.40, relwidth=0.62, relheight=0.08)
        
    
    lb4 = Label(labelFrame,text="Date of purchase : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.55, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.55, relwidth=0.62, relheight=0.08)
    
    lb5 = Label(labelFrame,text="Price : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.70, relheight=0.08)
        
    bookInfo5 = Entry(labelFrame)
    bookInfo5.place(relx=0.3,rely=0.70, relwidth=0.62, relheight=0.08)

    lb6 = Label(labelFrame,text="Quantity: ", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.85, relheight=0.08)
        
    bookInfo6 = Entry(labelFrame)
    bookInfo6.place(relx=0.3,rely=0.85, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=sales)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
