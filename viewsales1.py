
from tkinter import *
import tkinter.messagebox as m
from tkinter.ttk import *
import mysql.connector as mysql
from viewsales2 import *


def shows(a):
    global t1,root2
    searching = t1.get()
    print(a)
    if a==1:
        try:
            import mysql.connector as mysql
            db = mysql.connect(host="localhost",user="root",password="archi23",database="bookend")
            c = db.cursor()
            searchSQL = "select * from sales where custname = '"+searching+"'"
            c.execute(searchSQL)
            anyone = c.fetchall()
            db.commit()
            if len(anyone)==0:
                m.showinfo('SORRY',"NO RELEVANT RECORD FOUND!!!")
            else:
                root2.destroy()
                searchedRESULT(anyone)
                for i in anyone:
                    print(i)

        except:
            m.showinfo('SORRY',"ERROR OCCURED")
            
    elif a==2:
        try:
            import mysql.connector as mysql
            db = mysql.connect(host="localhost",user="root",password="archi23",database="bookend")
            c = db.cursor()
            searchSQL = "select * from sales where saledt = '"+searching+"'"
            c.execute(searchSQL)
            anyone = c.fetchall()
            db.commit()
            if len(anyone)==0:
                m.showinfo('SORRY',"NO RELEVANT RECORD FOUND!!!")
            else:
                root2.destroy()
                searchedRESULT(anyone)
            print("PURCHASE DATE",searching)
        except:
            m.showinfo('SORRY',"ERROR OCCURED")
    elif a==3:
        try:
            import mysql.connector as mysql
            db = mysql.connect(host="localhost",user="root",password="archi23",database="bookend")
            c = db.cursor()
            searchSQL = "select * from sales where BillID={}".format(searching)
            c.execute(searchSQL)
            anyone = c.fetchall()
            db.commit()
            if len(anyone)==0:
                m.showinfo('SORRY',"NO RELEVANT RECORD FOUND!!!")
            else:
                root2.destroy()
                searchedRESULT(anyone)
            print("BILL ID",searching)
        except:
            m.showinfo('SORRY',"ERROR OCCURED")   
    else:
        print("NOTHING")
        m.showinfo('SORRY',"CHECK INPUT VALUES")
    
    
    
        
def salesrecordss():
    global t1,t2,root2
    
    root2 = Tk()
    root2.configure(bg="red")
    root2.title("VIEW IN SALES RECORDS")
    root2.geometry("400x400")

    tt1 = Label(root2,text = "SEARCH OPTIONS", bg="red",fg="white",font=("Calibri",20))
    tt1.place(x=30,y=10)

    l1= Label(root2,text="value ")
    t1 =Entry(root2)

    l1.place(x=50,y=150)
    t1.place( x=150,y=150)

    l2= Label(root2,text="Categories ")

    pizza = IntVar()
    MODES = [
        ("CUSTOMER NAME",1),
        ("PURCHASE DATE",2),
        ("BILL ID",3),
    ]
    placing = 50
    for text,mode in MODES:
        r1 = Radiobutton(root2,text=text,variable = pizza, value=mode)
        r1.place(x=150, y= placing)
        placing = placing+30
        

    l2.place(x=50,y=50)
    
    tt5 = Label(root2,text = "NOTE!!! DATE IN YYYY-MM-DD FORMAT", bg="white",fg="black",font=("Calibri",10))
    tt5.place(x=30,y=200)

    b1  = Button(root2,text="Submit ",underline=2,command=lambda: shows(pizza.get()))
    b2  = Button(root2,text="QUIT ",command = root2.destroy)

    b1.place(x=150,y=250)
    b2.place( x=250,y=250)

    root2.mainloop()
