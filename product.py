from tkinter import* 
from tkinter import ttk
from tkinter import messagebox
import sqlite3
#https://www.youtube.com/watch?v=dOyrVtEcBDI&list=PL4P8sY6zvjk6ef4lpm6XiwJVRahLCp6DI&index=6 27:07

class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management Sytem | Developed By Ayush & Swagat")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()
       
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        
        product_Frame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=480)
        
        title = Label(product_Frame,text="Manage Product Details",font=("cambria",18),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)
        
        lbl_category = Label(product_Frame,text="Category",font=("cambria",18),bg="white").place(x=30,y=60)
        lbl_supplier = Label(product_Frame,text="Supplier",font=("cambria",18),bg="white").place(x=30,y=110)
        lbl_product_name = Label(product_Frame,text="Name",font=("cambria",18),bg="white").place(x=30,y=160)
        lbl_price = Label(product_Frame,text="Price",font=("cambria",18),bg="white").place(x=30,y=210)
        lbl_quantity = Label(product_Frame,text="Quantity",font=("cambria",18),bg="white").place(x=30,y=260)
        lbl_status = Label(product_Frame,text="Status",font=("cambria",18),bg="white").place(x=30,y=310)
        
        cmb_cat = ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state="readonly",justify=CENTER,font=("cambria",15))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)
        
        cmb_sup = ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,state="readonly",justify=CENTER,font=("cambria",15))
        cmb_sup.place(x=150,y=110,width=200)
        #cmb_sup.current(0)
        
        txt_name = Entry(product_Frame,textvariable=self.var_name,font=("cambria",15),bg="lightyellow").place(x=150,y=160,width=200)
        txt_price = Entry(product_Frame,textvariable=self.var_price,font=("cambria",15),bg="lightyellow").place(x=150,y=210,width=200)
        txt_qty = Entry(product_Frame,textvariable=self.var_qty,font=("cambria",15),bg="lightyellow").place(x=150,y=260,width=200)
        
        cmb_status = ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),state="readonly",justify=CENTER,font=("cambria",15))
        cmb_status.place(x=150,y=310,width=200)
        cmb_status.current(0)

        btn_add = Button(product_Frame,text="Save",font=("cambria",15),bg="#2196f3",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update = Button(product_Frame,text="Update",font=("cambria",15),bg="#2196f3",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete = Button(product_Frame,text="Delete",font=("cambria",15),bg="#2196f3",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear = Button(product_Frame,text="Clear",font=("cambria",15),bg="#2196f3",cursor="hand2").place(x=340,y=400,width=100,height=40)
        
        SearchFrame = LabelFrame(self.root,text="Search Product",font=("Cambria",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)

        cmb_search = ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name"),state="readonly",justify=CENTER,font=("cambria",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
        txt_search = Entry(SearchFrame,textvariable=self.var_searchtxt,font=("cambria",15),bg="lightyellow").place(x=200,y=10)
        btn_search = Button(SearchFrame,text="Search",font=("cambria",15),bg="green4",fg="white",cursor="hand2").place(x=435,y=9,width=150,height=30)

        p_frame = Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)
        
        scrolly = Scrollbar(p_frame,orient=VERTICAL)
        scrollx = Scrollbar(p_frame,orient=HORIZONTAL)
        
        self.productTable = ttk.Treeview(p_frame,columns=("pid","Category","Supplier","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)
        
        self.productTable.heading("pid",text="P ID")
        self.productTable.heading("Category",text="Category")
        self.productTable.heading("Supplier",text="Supplier")
        self.productTable.heading("name",text="Name")
        self.productTable.heading("price",text="Price")
        self.productTable.heading("qty",text="Qty")
        self.productTable.heading("status",text="Status")
        
        
        self.productTable["show"]="headings"
        
        self.productTable.column("pid",width=90)
        self.productTable.column("Category",width=100)
        self.productTable.column("Supplier",width=100)
        self.productTable.column("name",width=100)
        self.productTable.column("price",width=90)
        self.productTable.column("qty",width=100)
        self.productTable.column("status",width=100)

        self.productTable.pack(fill=BOTH,expand=1)

        self.show()

    def fetch_cat_sup(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select name from category")
            cat=cur.fetchall()
            self.cat_list.append("Empty")
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("Select name from supplier")
            sup=cur.fetchall()
            print(sup)
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_sup.get()=="Select" or self.var_name.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product already present, try different", parent=self.root)
                else:
                    cur.execute("Insert into product (Category,Supplier,name,price,qty,status) values(?,?,?,?,?,?,?)",(
                                    self.var_cat.get(),
                                    self.var_sup.get(),
                                    self.var_name.get(),
                                    self.var_price.get(),
                                    self.var_qty.get(),
                                    self.var_status.get(),                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[9])
        self.var_salary.set(row[10])

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID", parent=self.root)
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                                    
                                    self.var_name.get(),
                                    self.var_email.get(),
                                    self.var_gender.get(),
                                    self.var_contact.get(),
                                    self.var_dob.get(),
                                    self.var_doj.get(),
                                    self.var_pass.get(),
                                    self.var_utype.get(),
                                    self.txt_address.get('1.0',END),
                                    self.var_salary.get(),
                                    self.var_emp_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated Successfully",parent=self.root)
                    self.show()
                    con.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()

        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete?",parent=self.root)
                    if op==True:                        
                        cur.execute("Delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee Deleted Successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def clear(self):
        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_contact.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_pass.set(""),
        self.var_utype.set("Admin"),
        self.txt_address.delete('1.0',END),
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search Input is required",parent=self.root)
                
            else:
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

        
if __name__=="__main__":
    root=Tk()
    obj=productClass(root)
    root.mainloop()