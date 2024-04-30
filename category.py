from tkinter import*
from tkinter import ttk, messagebox
import sqlite3
#https://www.youtube.com/watch?v=_9vVIrJoC34&list=PL4P8sY6zvjk6ef4lpm6XiwJVRahLCp6DI&index=5 19:16

class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Ayush & Swagat")
        self.root.config(bg="white")
        self.root.focus_force()
        #--------------------Variables
        self.var_cat_id = StringVar()
        self.var_name = StringVar()
        
        #-------------------title--------------
        lbl_title = Label(self.root,text="Manage Product Category",font=("cambria",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        
        lbl_name = Label(self.root,text="Enter Category Name",font=("cambria",20),bg="white").place(x=50,y=100)
        
        text_name = Entry(self.root,textvariable=self.var_name,font=("cambria",18),bg="lightyellow").place(x=50,y=170,width=320)
        btn_add = Button(self.root,text="Add",command=self.add,font=("cambria",15),bg="#4caf50",fg="white",cursor="hand2").place(x=50,y=220,width=150,height=30)
        btn_delete = Button(self.root,text="Delete",command=self.delete,font=("cambria",15),bg="red",fg="white",cursor="hand2").place(x=220,y=220,width=150,height=30)
        
        #--------------------------Category Details
        cat_frame = Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=380,height=350)
        
        scrolly = Scrollbar(cat_frame,orient=VERTICAL)
        scrollx = Scrollbar(cat_frame,orient=HORIZONTAL)
        
        self.categoryTable = ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)
        
        self.categoryTable.heading("cid",text="C ID")
        self.categoryTable.heading("name",text="NAME")
        self.categoryTable["show"]="headings"        
        self.categoryTable.column("cid",width=90)
        self.categoryTable.column("name",width=100)
        self.categoryTable.pack(fill=BOTH,expand=1)
        self.categoryTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
    
    #-----------------functions--------------
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category Name must be required",parent=self.root)
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category already present, try different", parent=self.root)
                else:
                    cur.execute("Insert into category (name) values(?)",(self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Category Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def get_data(self,ev):
        f=self.categoryTable.focus()
        content=(self.categoryTable.item(f))
        row=content['values']
        
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()

        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Please select Category from the list",parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Error, please try again", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete?",parent=self.root)
                    if op==True:                        
                        cur.execute("Delete from category where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Category Deleted Successfully",parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
        
        
if __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()