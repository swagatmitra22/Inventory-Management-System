from tkinter import* 
from tkinter import ttk,messagebox
import sqlite3

class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management Sytem | Developed By Ayush & Swagat")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        
        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()

        lbl_search = Label(self.root,text="Invoice No.",bg="white",font=("cambria",15))
        lbl_search.place(x=700,y=80)
        
        
        txt_search = Entry(self.root,textvariable=self.var_searchtxt,font=("cambria",15),bg="lightyellow").place(x=810,y=80,width=160)
        btn_search = Button(self.root,text="Search",command=self.search,font=("cambria",15),bg="green4",fg="white",cursor="hand2").place(x=980,y=79,width=100,height=30)
        
        title = Label(self.root,text="Supplier Details",font=("cambria",20,"bold"),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)

        lbl_supplier_invoice = Label(self.root,text="Invoice No.",font=("cambria",15),bg="white").place(x=50,y=80)   
        txt_supplier_invoice = Entry(self.root,textvariable=self.var_sup_invoice,font=("cambria",15),bg="lightyellow").place(x=180,y=80,width=180)
        
        lbl_name = Label(self.root,text="Name",font=("cambria",15),bg="white").place(x=50,y=120)
        txt_name = Entry(self.root,textvariable=self.var_name,font=("cambria",15),bg="lightyellow").place(x=180,y=120,width=180)
        
        lbl_contact = Label(self.root,text="Contact",font=("cambria",15),bg="white").place(x=50,y=160)
        txt_contact = Entry(self.root,textvariable=self.var_contact,font=("cambria",15),bg="lightyellow").place(x=180,y=160,width=180)
        
        lbl_desc = Label(self.root,text="Description",font=("cambria",15),bg="white").place(x=50,y=200)
        self.txt_desc = Text(self.root,font=("cambria",15),bg="lightyellow")
        self.txt_desc.place(x=180,y=200,width=470,height=90)
        
        btn_add = Button(self.root,text="Save",command=self.add,font=("cambria",15),bg="#2196f3",cursor="hand2").place(x=180,y=370,width=110,height=35)
        btn_update = Button(self.root,text="Update",command=self.update,font=("cambria",15),bg="#4caf50",cursor="hand2").place(x=300,y=370,width=110,height=35)
        btn_delete = Button(self.root,text="Delete",command=self.delete,font=("cambria",15),bg="#f44336",cursor="hand2").place(x=420,y=370,width=110,height=35)
        btn_clear = Button(self.root,text="Clear",command=self.clear,font=("cambria",15),bg="#607d8b",cursor="hand2").place(x=540,y=370,width=110,height=35)
        
        emp_frame = Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=120,width=380,height=350)
        
        scrolly = Scrollbar(emp_frame,orient=VERTICAL)
        scrollx = Scrollbar(emp_frame,orient=HORIZONTAL)
        
        self.SupplierTable = ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)
        
        self.SupplierTable.heading("invoice",text="INVOICE NO.")
        self.SupplierTable.heading("name",text="NAME")
        self.SupplierTable.heading("contact",text="CONTACT")
        self.SupplierTable.heading("desc",text="DESCRIPTION")
        
        self.SupplierTable["show"]="headings"
        
        self.SupplierTable.column("invoice",width=90)
        self.SupplierTable.column("name",width=100)
        self.SupplierTable.column("contact",width=100)
        self.SupplierTable.column("desc",width=100)
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice No. already assigned, try different", parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,desc) values(?,?,?,?)",(
                                    self.var_sup_invoice.get(),
                                    self.var_name.get(),
                                    self.var_contact.get(),
                                    self.txt_desc.get('1.0',END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def get_data(self,ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['values']
        
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[3])

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No.", parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(
                                    
                                    self.var_name.get(),                
                                    self.var_contact.get(),                                   
                                    self.txt_desc.get('1.0',END),
                                    self.var_sup_invoice.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully",parent=self.root)
                    self.show()
                    con.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()

        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No.", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete?",parent=self.root)
                    if op==True:                        
                        cur.execute("Delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def clear(self):
        self.var_sup_invoice.set(""),
        self.var_name.set(""),
        self.var_contact.set(""),
        self.txt_desc.delete('1.0',END),
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice No. is required",parent=self.root)
                
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")


if __name__=="__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()