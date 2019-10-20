from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
f=open("database_proj",'a+')

root = Tk()
root.title("Stationary ShopManagment System")
root.configure(width=1500,height=600,bg="Grey")
var=-1
#All functions

def additem():
    global var
    num_lines = 0
    with open("database_proj", 'r') as f10:
        for line in f10:
            num_lines += 1
    var=num_lines-1
    e1= entry1.get()
    e2=entry2.get()
    e3=entry3.get()
    e4=entry4.get()
    e5=entry5.get()
    f.write('{0} {1} {2} {3} {4}\n'.format(str(e1),e2,e3,str(e4),e5))
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    messagebox.showinfo("ADD ITEM", "ITEM ADDED SUCCESSFULLY....!!!!!")

def deleteitem():
    e1=entry1.get()
    with open(r"database_proj") as f, open(r"database_proj1", "w") as working:
        for line in f:
            if str(e1) not in line:
                working.write(line)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    os.remove(r"database_proj")
    os.rename(r"database_proj1", r"database_proj")
    f.close()
    working.close()

def list1():
    global var
    var=0
    f.seek(var)
    root1 = Tk()
    root1.configure(bg="Grey")
    root1.title("Stationary Store Database")
    scrollbar = Scrollbar(root1)
    scrollbar.pack( side = RIGHT, fill = Y)
    mytext = Text(root1, yscrollcommand = scrollbar.set ,width=24,height= 18 ,bg= "gray",fg="black", font=("Times", 16))
    string = f.read()
    mytext.insert(END,string)
    mytext.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mytext.yview )

def searchitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    i=0
    flag = 1
    e1 = entry6.get()
    with open(r"database_proj") as working:
        for line in working:
            i=i+1
            if str(e1) in line:
                flag = 0
                break
        try:
           if flag != 1:
                v = list(line.split(" "))
                entry1.delete(0, END)
                entry2.delete(0, END)
                entry3.delete(0, END)
                entry4.delete(0, END)
                entry5.delete(0, END)
                entry1.insert(0, str(v[0]))
                entry2.insert(0, str(v[1]))
                entry3.insert(0, str(v[2]))
                entry4.insert(0, str(v[3]))
                entry5.insert(0, str(v[4]))

        except:
            messagebox.showinfo("Title", "error end of file")

        if flag !=0:
            messagebox.showinfo("Title", "NOT FOUND")
    working.close()

def clearitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)


def qExit():
    qExit= messagebox.askyesno("Quit The System","Do you want to quit(y/n)?")
    if qExit > 0:
        root.destroy()
        return

#All labels Entrys Button grid place
label0= Label(root,text="STATIONARY SHOP MANAGEMENT SYSTEM ",bg="Black",fg="#F9FAE9",font=("Times", 30))
label1=Label(root,text="ENTER ITEM NAME",bg="black",relief="ridge",fg="white",bd=8,font=("Times", 12),width=25)
entry1=Entry(root , font=("Times", 14),bd=8,width=25,bg="white")
label2=Label(root, text="ENTER ITEM PRICE",relief="ridge",height="1",bg="black",bd=8,fg="white", font=("Times", 12),width=25)
entry2= Entry(root, font=("Times", 14),bd=8,width=25,bg="white")
label3=Label(root, text="ENTER ITEM QUANTITY",relief="ridge",bg="black",bd=8,fg="white", font=("Times", 12),width=25)
entry3= Entry(root, font=("Times", 14),bd=8,width=25,bg="white")
label4=Label(root, text="ENTER ITEM CATEGORY",relief="ridge",bg="black",bd=8,fg="white", font=("Times", 12),width=25)
entry4= Entry(root, font=("Times", 14),bd=8,width=25,bg="white")
label5=Label(root, text="ENTER ITEM DISCOUNT",bg="black",relief="ridge",fg="white",bd=8, font=("Times", 12),width=25)
entry5= Entry(root, font=("Times", 14),bd=8,width=25,bg="white")
buttoncolor="#49D810"
buttonfg="black"
button1= Button(root,highlightcolor="red",activebackground="green", text="ADD ITEM",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=additem)
button2= Button(root,highlightcolor="red",activebackground="green", text="DELETE ITEM",bd=8, bg=buttoncolor, fg=buttonfg, width =25, font=("Times", 12),command=deleteitem)
button3= Button(root,highlightcolor="red",activebackground="green", text="VIEW DATABASE",bd=8, bg=buttoncolor, fg=buttonfg, width =25, font=("Times", 12),command=list1)
button4= Button(root,highlightcolor="red",activebackground="green", text="SEARCH ITEM",bd=8, bg=buttoncolor, fg=buttonfg, width =25, font=("Times", 12),command=searchitem)
button5= Button(root,highlightcolor="red",activebackground="green", text="CLEAR SCREEN",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=clearitem)
button6= Button(root,highlightcolor="blue",activebackground="red", text="Exit",bd=8, bg="#FF0000", fg="#EEEEF1", width=25, font=("Times", 40),command=qExit)
entry6= Entry(root, font=("Times", 14),justify='left',bd=8,width=25,bg="#EEEEF1")

label0.grid(columnspan=6, padx=1, pady=10)
label1.grid(row=1,column=0, padx=10, pady=10)
label2.grid(row=2,column=0, padx=10, pady=10)
label3.grid(row=3,column=0, padx=10, pady=10)
label4.grid(row=4,column=0, padx=10, pady=10)
label5.grid(row=5,column=0, padx=10, pady=10)
entry1.grid(row=1,column=1, padx=40, pady=10)
entry2.grid(row=2,column=1, padx=10, pady=10)
entry3.grid(row=3,column=1, padx=10, pady=10)
entry4.grid(row=4,column=1, padx=10, pady=10)
entry5.grid(row=5,column=1, padx=10, pady=10)
entry6.grid(row=1,column=3, padx=10, pady=10)
button1.grid(row=6,column=0, padx=10, pady=10)
button2.grid(row=6,column=1, padx=40, pady=10)
button3.grid(row=3,column=3, padx=40, pady=10)
button4.grid(row=2,column=3, padx=40, pady=10)
button5.grid(row=4,column=3, padx=40, pady=10)
button6.place(x=635,y=337,height= 102,width=245)

root.mainloop()
