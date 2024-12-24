from tkinter import *
from tkinter import messagebox as m
import mysql.connector as mysql
db = mysql.connect(host="localhost",user="root",password="archi23",database="bookend")
cur = db.cursor()

def searchedRESULT(parass): 
    
    root3 = Tk()
    root3.title("BOOK STORE MANAGEMENT SYSTEM")
    root3.minsize(width=400,height=400)
    root3.geometry("600x500")


    Canvas3 = Canvas(root3) 
    Canvas3.config(bg="#12a4d9")
    Canvas3.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root3,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="SALES RECORD", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root3,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    Label(labelFrame, text="%-10s%-40s%-30s%-20s"%('BIllID','CUSTOMER NAME','BOOK ID','PURCHASE DATE'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    
    try:
        print(type(parass))
        for i in parass:
            Label(labelFrame, text="%-10s%-30s%-30s%-20s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        m.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root3,text="Quit",bg='#f7f1e3', fg='black', command=root3.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root3.mainloop()

