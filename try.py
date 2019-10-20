from tkinter import *
from tkinter import messagebox
import mysql.connector
mydb = mysql.connector.connect(host= "localhost",user = "root",passwd="root")
my_cursor = mydb.cursor()
##############################################################################################
my_cursor.execute("create database if not exists Store")
my_cursor.execute("use Store")
my_cursor.execute("create table if not exists stationary(item_name VARCHAR(20) not null unique, item_price INTEGER(10), item_quantity INTEGER(10), item_category VARCHAR(20), item_discount float(3), item_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
##############################################################################################
root = Tk()
root.title("Stationary Shop Managment System")
root.configure(width=1500,height=600,bg="Grey")

buttoncolor = "#49D810"
buttonfg = "black"



#All functions

def additem():

	try:
		e1=entry1.get()
		e2=entry2.get()
		e3=entry3.get()
		e4=entry4.get()
		e5=entry5.get()
		sql = "INSERT INTO stationary (item_name, item_price, item_quantity, item_category, item_discount) VALUES (%s, %s, %s, %s, %s)"
		val = (str(e1),e2,e3,str(e4),e5)
		my_cursor.execute(sql,val)
		mydb.commit()
		entry1.delete(0, END)
		entry2.delete(0, END)
		entry3.delete(0, END)
		entry4.delete(0, END)
		entry5.delete(0, END)
		messagebox.showinfo(" ADD ITEM ", "ITEM ADDED SUCCESSFULLY")
	except (mysql.connector.Error,mysql.connector.Warning) as e:
		messagebox.showerror("Duplicate Data","You are trying to insert a item which is already present in database")

def delete1():
    e6 = entry6.get()
    my_cursor.execute("delete from stationary where item_name = '{0}'".format(str(e6)))
    mydb.commit()
    messagebox.showinfo("DELETE ITEM", "ITEM DELETED SUCCESSFULLY")

def showdatabase():
    root1 = Tk()
    root1.configure(bg="Grey")
    root1.title("Stationary Store Management Database")
    my_cursor.execute("select * from stationary")
    mytext1 = my_cursor.fetchall()
    mytext = Text(root1,width=90,height= 20 ,bg= "gray",fg="black", font=("Times", 12))
    mytext.insert(END," Item_Name \t\tItem_Price \t\tItem_Quantity \t\tItem_Category \t\tItem_Discount \n")
    mytext.insert(END," ------------ \t\t----------- \t\t-------------- \t\t--------------- \t\t--------------- \n")
    for row in mytext1:
        mytext.insert(END,"       {0} \t\t     {1} \t\t         {2} \t\t   {3} \t\t          {4}\n".format(row[0],row[1],row[2],row[3],row[4]))
    mytext.pack( side = LEFT)

def searchitem():
	entry1.delete(0, END)
	entry2.delete(0, END)
	entry3.delete(0, END)
	entry4.delete(0, END)
	entry5.delete(0, END)
	e6 = entry6.get()
	if e6 == "SEARCH" or e6 == "":{
		messagebox.showinfo("Warning","Please first enter Item name in search bar")
	}
	else:
		my_cursor.execute("select * from stationary where item_name = '{0}'".format(str(e6)))
		mytext1 = my_cursor.fetchone()
		if mytext1 == None:
			messagebox.showinfo("Error","Element not exist in database")
		else:
			entry1.insert(0,mytext1[0])
			entry2.insert(0,mytext1[1])
			entry3.insert(0,mytext1[2])
			entry4.insert(0,mytext1[3])
			entry5.insert(0,mytext1[4])
			entry6.delete(0, END)
			entry6.insert(0,"SEARCH")

def update():
	e6 = entry6.get()
	if e6 == "SEARCH" or e6 == "":
		messagebox.showinfo("Warning","Enter the item in search bar first")

	else:
		my_cursor.execute("select * from stationary where item_name = '{0}'".format(str(e6)))
		line = my_cursor.fetchone()
		if line != None:
			iname = line[0]
			iprice = line[1]
			iquantity = line[2]
			icategory = line[3]
			idiscount = line[4]

			root2 = Tk()
			root2.title("Update Records")
			root2.configure(width=900,height=500,bg="Grey")

			def actualupdate():
				e1 = uentry1.get()
				e2 = uentry2.get()
				e3 = uentry3.get()
				e4 = uentry4.get()
				e5 = uentry5.get()
				
				if e1!="Update" or e1!="":
					iname=e1
				if e2!="Update" or e1!="":
					iprice=e2
				if e3!="Update" or e1!="":
					iquantity=e3
				if e4!="Update" or e1!="":
					icategory=e4
				if e5!="Update" or e1!="":
					idiscount=e5
				sql = "update stationary set item_name = %s, item_price = %s, item_quantity = %s, item_category = %s, item_discount = %s  where item_name = %s"
				val = (str(iname),iprice,iquantity,str(icategory),idiscount,str(e6))
				my_cursor.execute(sql,val)
				mydb.commit()
				messagebox.showinfo("UPDATE ITEM", "ITEM UPDATED SUCCESSFULLY")
				uentry1.delete(0, END)
				uentry2.delete(0, END)
				uentry3.delete(0, END)
				uentry4.delete(0, END)
				uentry5.delete(0, END)
				root2.destroy()

			def clearuitem():
				uentry1.delete(0, END)
				uentry2.delete(0, END)
				uentry3.delete(0, END)
				uentry4.delete(0, END)
				uentry5.delete(0, END)


			#Labels, Entries and button for root2 window.
			button8 = Button(root2,activebackground="green", text="UPDATE ITEM",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=actualupdate)
			button9 = Button(root2,activebackground="green", text="CLEAR",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=clearuitem)
			ulabel0 = Label(root2,text="UPDATE RECORD",bg="Black",fg="#F9FAE9",font=("Times", 30),width=23)
			ulabel1 = Label(root2,text="ENTER ITEM NAME",bg="black",relief="ridge",fg="white",bd=8,font=("Times", 12),width=25)
			uentry1 = Entry(root2, font=("Times", 14),bd=8,width=25,bg="white")
			ulabel2 = Label(root2, text="ENTER ITEM PRICE",relief="ridge",height="1",bg="black",bd=8,fg="white", font=("Times", 12),width=25)
			uentry2 = Entry(root2, font=("Times", 14),bd=8,width=25,bg="white")
			ulabel3 = Label(root2, text="ENTER ITEM QUANTITY",relief="ridge",bg="black",bd=8,fg="white", font=("Times", 12),width=25)
			uentry3 = Entry(root2, font=("Times", 14),bd=8,width=25,bg="white")
			ulabel4 = Label(root2, text="ENTER ITEM CATEGORY",relief="ridge",bg="black",bd=8,fg="white", font=("Times", 12),width=25)
			uentry4 = Entry(root2, font=("Times", 14),bd=8,width=25,bg="white")
			ulabel5 = Label(root2, text="ENTER ITEM DISCOUNT",bg="black",relief="ridge",fg="white",bd=8, font=("Times", 12),width=25)
			uentry5 = Entry(root2, font=("Times", 14),bd=8,width=25,bg="white")
			ulabel0.grid(columnspan=6, padx=10, pady=10)
			ulabel1.grid(row=1,column=0, padx=10, pady=10)
			ulabel2.grid(row=2,column=0, padx=10, pady=10)
			ulabel3.grid(row=3,column=0, padx=10, pady=10)
			ulabel4.grid(row=4,column=0, padx=10, pady=10)
			ulabel5.grid(row=5,column=0, padx=10, pady=10)
			uentry1.grid(row=1,column=1, padx=10, pady=10)
			uentry2.grid(row=2,column=1, padx=10, pady=10)
			uentry3.grid(row=3,column=1, padx=10, pady=10)
			uentry4.grid(row=4,column=1, padx=10, pady=10)
			uentry5.grid(row=5,column=1, padx=10, pady=10)
			button8.grid(row=6,column=1, padx=10, pady=10)
			button9.grid(row=6,column=0,padx=10,pady=10)

			uentry1.insert(0,iname)
			uentry2.insert(0,iprice)
			uentry3.insert(0,iquantity)
			uentry4.insert(0,icategory)
			uentry5.insert(0,idiscount)
			entry6.insert(0,"SEARCH")

			entry1.delete(0, END)
			entry2.delete(0, END)
			entry3.delete(0, END)
			entry4.delete(0, END)
			entry5.delete(0, END)
			entry6.delete(0, END)
		else:
			messagebox.showinfo("Error","Element does not exist.")

def clearitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)

def qExit():
    qExit= messagebox.askyesno("Quit System","Do you want to quit(y/n)?\nThank You!!!!!!")
    if qExit > 0:
        root.destroy()
        return


#All labels Entrys Button grid place
label0 = Label(root,text="STATIONARY STORE MANAGEMENT SYSTEM ",bg="Black",fg="#F9FAE9",font=("Times", 27),width=39)
label1 = Label(root,text="ENTER ITEM NAME",bg="black",relief="ridge",fg="white",bd=8,font=("Times", 12),width=25)
entry1 = Entry(root , font=("Times", 14),bd=8,width=25,bg="white")
label2 = Label(root, text="ENTER ITEM PRICE",relief="ridge",height="1",bg="black",bd=8,fg="white", font=("Times", 12),width=25)
entry2 = Entry(root, font=("Times", 14),bd=8,width=25,bg="white")
label3 = Label(root, text="ENTER ITEM QUANTITY",relief="ridge",bg="black",bd=8,fg="white", font=("Times", 12),width=25)
entry3 = Entry(root, font=("Times", 14),bd=8,width=25,bg="white")
label4 = Label(root, text="ENTER ITEM CATEGORY",relief="ridge",bg="black",bd=8,fg="white", font=("Times", 12),width=25)
entry4 = Entry(root, font=("Times", 14),bd=8,width=25,bg="white")
label5 = Label(root, text="ENTER ITEM DISCOUNT",bg="black",relief="ridge",fg="white",bd=8, font=("Times", 12),width=25)
entry5 = Entry(root, font=("Times", 14),bd=8,width=25,bg="white")
button1 = Button(root,activebackground="green", text="ADD ITEM",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=additem)
button2 = Button(root,activebackground="green", text="DELETE ITEM",bd=8, bg=buttoncolor, fg=buttonfg, width =25, font=("Times", 12),command=delete1)
button3 = Button(root,activebackground="green", text="VIEW DATABASE",bd=8, bg=buttoncolor, fg=buttonfg, width =25, font=("Times", 12),command=showdatabase)
button4 = Button(root,activebackground="green", text="SEARCH ITEM",bd=8, bg=buttoncolor, fg=buttonfg, width =25, font=("Times", 12),command=searchitem)
button5 = Button(root,activebackground="green", text="CLEAR SCREEN",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=clearitem)
button6 = Button(root,activebackground="red", text="EXIT",bd=8, bg="#FF0000", fg="#EEEEF1", width=25, font=("Times", 12),command=qExit)
entry6 = Entry(root, font=("Times", 14),justify='left',bd=8,width=25,bg="#EEEEF1")
entry6.insert(0,"SEARCH")
button7 = Button(root,activebackground="green", text="UPDATE ITEM",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=update)
########POSITION OF ALL BUTTONS AND ENTRY
label0.grid(columnspan=6, padx=10, pady=10)
label1.grid(row=1,column=0, padx=10, pady=10)
label2.grid(row=2,column=0, padx=10, pady=10)
label3.grid(row=3,column=0, padx=10, pady=10)
label4.grid(row=4,column=0, padx=10, pady=10)
label5.grid(row=5,column=0, padx=10, pady=10)
entry1.grid(row=1,column=1, padx=10, pady=10)
entry2.grid(row=2,column=1, padx=10, pady=10)
entry3.grid(row=3,column=1, padx=10, pady=10)
entry4.grid(row=4,column=1, padx=10, pady=10)
entry5.grid(row=5,column=1, padx=10, pady=10)
entry6.grid(row=1,column=2, padx=10, pady=10)
button1.grid(row=6,column=0, padx=10, pady=10)
button2.grid(row=6,column=1, padx=10, pady=10)
button3.grid(row=3,column=2, padx=10, pady=10)
button4.grid(row=2,column=2, padx=10, pady=10)
button5.grid(row=4,column=2, padx=10, pady=10)
button6.grid(row=6,column=2, padx=10, pady=10)
button7.grid(row=5,column=2, padx=10, pady=10)

root.mainloop()
