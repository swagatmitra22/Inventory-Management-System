from tkinter import* 
from PIL import Image,ImageTk
from employee import employeeClass
# from supplier import supplierClass
# from category import categoryClass
# from product import productClass
# from sales import salesClass

class IMS:
    def _init_(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by Ayush & Swagat❤")
        self.root.config(bg="white")
        #-----------------title----------------
        title = Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        
        #---------btn Logout
        btn_logout = Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        
        #-----------------clock----------------
        self.lbl_clock = Label(self.root,text="Welcome to Inventory Management System \t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS",font=("times new roman",15,"bold"),bg="#010c48",fg="white",anchor="w",padx=20)
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        #------------LEft Menu
        #MenuLogo
        LeftMenu = Frame(self.root, bd=2,relief = RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)
        
        lbl_menu = Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        
        btn_employee = Button(LeftMenu,text="Employee",command=self.employee,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Supplier = Button(LeftMenu,text="Supplier",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Category = Button(LeftMenu,text="category",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Product = Button(LeftMenu,text="Product",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Sales = Button(LeftMenu,text="Sales",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Exit = Button(LeftMenu,text="Exit",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #-----------------------------Content-----------------
        self.lbl_employee = Label(self.root,text="Total Employee\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("gouldy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)
        
        self.lbl_supplier = Label(self.root,text="Total Supplier\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("gouldy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)
        
        self.lbl_category = Label(self.root,text="Total Category\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("gouldy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)
        
        self.lbl_product = Label(self.root,text="Total Product\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("gouldy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)
        
        self.lbl_sales = Label(self.root,text="Total Sales\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("gouldy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)

        #-----------------------footer--------------------
        lbl_footer = Label(self.root,text="IMS-Inventory Management System | Developed by Ayush & Swagat❤\nFor any technical Issues Contact xxxxxxxxxx",font=("times new roman",12,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).pack(side=BOTTOM, fill=X)
        
      
#-----------------------------------------------------------------
    def employee(self):
        self.new.win = Toplevel(self,root)
        self.new_obj = employeeClass(self.new_win)

  
if _name=="main_":
    root = Tk()
    obj = IMS(root)
    root.mainloop()