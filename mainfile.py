from tkinter import *
import mysql.connector as mysql

from addbook import *
from deletebook import *
from viewbook import *
from addsales import *
from viewsales1 import *
from viewsales2 import *
db= mysql.connect(host="localhost",user="root",password="archi23",database="bookend")
cur=db.cursor()

root=Tk()
root.title("BOOK STORE MANAGEMENT SYSTEM")
root.minsize(width=500,height=500)
root.geometry("600x500")

same=True


Canvas1 = Canvas(root)

Canvas1.config(bg="grey")
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Books'n'Things", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Book Details",bg='black', fg='white',command=addBook)
btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book Details",bg='black', fg='white', command=delete)
btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Add sales record",bg='black', fg='white', command = salesadd)
btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text=" View Order details",bg='black', fg='white', command = salesrecordss)
btn5.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

btn6 = Button(root,text=" QUIT",bg='black', fg='white', command = root.destroy)
btn6.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()



