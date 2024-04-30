from tkinter import* 
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass


class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x690+0+0")
        self.root.title("Inventory Management System | Developed by Ayush & Swagat")
        
        title = Label(self.root,text="Inventory Management System",font=("cambria",30,"bold"),bg="IndianRed4",fg="white",anchor='w',padx=20).place(x=0,y=0,relwidth=1,height=70)
    
        btn_logout = Button(self.root,text="Logout",font=("cambria",15,"bold"),bg="orange2",cursor="hand2").place(x=1175,y=10,height=50,width=150)
        
        self.lbl_clock = Label(self.root,text="Welcome to Inventory Management System \t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS",font=("cambria",15),bg="IndianRed2",fg="white",padx=20)
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #-----------Left Menu--------
        LeftMenu = Frame(self.root, bd=2,relief = RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_menu = Label(LeftMenu,text="Menu",font=("cambria",20,"bold"),bg="orange2")
        lbl_menu.pack(side=TOP,fill=X)

        btn_employee = Button(LeftMenu, text="Employee", command=self.employee, font=("cambria", 20, "bold"), bg="LightYellow2", bd=3, cursor="hand2")
        btn_employee.pack(side=TOP, fill=BOTH, expand=True)

        btn_Supplier = Button(LeftMenu,text="Supplier",command=self.supplier,font=("cambria",20,"bold"),bg="LightYellow2",bd=3,cursor="hand2")
        btn_Supplier.pack(side=TOP,fill=BOTH,expand=True)

        btn_Category = Button(LeftMenu,text="Category",command=self.category,font=("cambria",20,"bold"),bg="LightYellow2",bd=3,cursor="hand2")
        btn_Category.pack(side=TOP,fill=BOTH,expand=True)

        btn_Product = Button(LeftMenu,text="Product",command=self.product,font=("cambria",20,"bold"),bg="LightYellow2",bd=3,cursor="hand2")
        btn_Product.pack(side=TOP,fill=BOTH,expand=True)

        btn_Sales = Button(LeftMenu,text="Sales",command=self.sales,font=("cambria",20,"bold"),bg="LightYellow2",bd=3,cursor="hand2")
        btn_Sales.pack(side=TOP,fill=BOTH,expand=True)

        btn_Exit = Button(LeftMenu,text="Exit",font=("cambria",20,"bold"),bg="LightYellow2",bd=3,cursor="hand2")
        btn_Exit.pack(side=TOP,fill=BOTH,expand=True)

        self.lbl_employee = Label(self.root,text="Total Employee\n[0]",bd=5,relief=RIDGE,bg="IndianRed4",fg="white",font=("cambria",20,"bold"))
        self.lbl_employee.place(x=300,y=140,height=150,width=300)
        
        self.lbl_supplier = Label(self.root,text="Total Supplier\n[0]",bd=5,relief=RIDGE,bg="IndianRed4",fg="white",font=("cambria",20,"bold"))
        self.lbl_supplier.place(x=650,y=140,height=150,width=300)
        
        self.lbl_category = Label(self.root,text="Total Category\n[0]",bd=5,relief=RIDGE,bg="IndianRed4",fg="white",font=("cambria",20,"bold"))
        self.lbl_category.place(x=1000,y=140,height=150,width=300)
        
        self.lbl_product = Label(self.root,text="Total Product\n[0]",bd=5,relief=RIDGE,bg="IndianRed4",fg="white",font=("cambria",20,"bold"))
        self.lbl_product.place(x=300,y=330,height=150,width=300)
        
        self.lbl_sales = Label(self.root,text="Total Sales\n[0]",bd=5,relief=RIDGE,bg="IndianRed4",fg="white",font=("cambria",20,"bold"))
        self.lbl_sales.place(x=650,y=330,height=150,width=300)

        lbl_footer = Label(self.root,text="IMS-Inventory Management System | Developed with ❤ by Ayush & Swagat",font=("cambria",12),bg="black",fg="white",padx=20).pack(side=BOTTOM, fill=X)

    def employee(self):
        self.new = Toplevel(self.root)
        self.obj = employeeClass(self.new)

    def supplier(self):
        self.new = Toplevel(self.root)
        self.obj = supplierClass(self.new)

    def category(self):
        self.new = Toplevel(self.root)
        self.obj = categoryClass(self.new)
    
    def product(self):
        self.new = Toplevel(self.root)
        self.obj = productClass(self.new)

    def sales(self):
        self.new = Toplevel(self.root)
        self.obj = salesClass(self.new)

if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()