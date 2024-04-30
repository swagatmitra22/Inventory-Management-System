from tkinter import* 
from tkinter import ttk
from tkinter import messagebox
from employee import employeeClass
# from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass


class billClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x690+0+0")
        self.root.title("Inventory Management System | Developed by Ayush & Swagat")
        
        title = Label(self.root,text="Inventory Management System",font=("cambria",30,"bold"),bg="IndianRed4",fg="white",anchor='w',padx=20).place(x=0,y=0,relwidth=1,height=70)
    
        btn_logout = Button(self.root,text="Logout",font=("cambria",15,"bold"),bg="orange2",cursor="hand2").place(x=1175,y=10,height=50,width=150)
        
        self.lbl_clock = Label(self.root,text="Welcome to Inventory Management System \t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS",font=("cambria",15),bg="IndianRed2",fg="white",padx=20)
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #-----------------------PRODUCT FRAME---------------
        self.var_search = StringVar()
        productFrame1 = Frame(self.root,bd=4,relief=RIDGE,bg="white")
        productFrame1.place(x=6,y=110,width=410,height=550)

        pTitle = Label(productFrame1,text="ALl Products",font=("cambria",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)

        #----------------------Product Search Frame---------------------
        productFrame2 = Frame(productFrame1,bd=4,relief=RIDGE,bg="white")
        productFrame2.place(x=2,y=42,width=398,height=90)
        
        lbl_search = Label(productFrame2,text="Search Product | By Name",font=("cambria",15,"bold"),bg="white",fg="green").place(x=2,y=5)

        lbl_search = Label(productFrame2,text="Product Name",font=("cambria",15,"bold"),bg="white").place(x=2,y=45)
        txt_search = Entry(productFrame2,textvariable=self.var_search,font=("cambria",15),bg="lightyellow").place(x=138,y=47,width=150,height=22)
        btn_search = Button(productFrame2,text="Search",font=("cambria",15,),bg="#2196f3",fg="white",cursor="hand2").place(x=292,y=45,width=90,height=25)
        btn_show_all = Button(productFrame2,text="Show All",font=("cambria",15,),bg="#083591",fg="white",cursor="hand2").place(x=292,y=10,width=90,height=25)
        
        #----------------------Product Details Frame---------------------
        productFrame3 = Frame(productFrame1,bd=3,relief=RIDGE)
        productFrame3.place(x=2,y=140,width=398,height=380)
        
        scrolly = Scrollbar(productFrame3,orient=VERTICAL)
        scrollx = Scrollbar(productFrame3,orient=HORIZONTAL)
        
        self.product_table = ttk.Treeview(productFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        
        self.product_table.heading("pid",text="P ID")
        self.product_table.heading("name",text="NAME")
        self.product_table.heading("price",text="PRICE")
        self.product_table.heading("qty",text="QTY")
        self.product_table.heading("status",text="Status")

        self.product_table["show"]="headings"
        
        self.product_table.column("pid",width=90)
        self.product_table.column("name",width=100)
        self.product_table.column("price",width=100)
        self.product_table.column("qty",width=100)
        self.product_table.column("status",width=90)
        self.product_table.pack(fill=BOTH,expand=1)
        #self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note = Label(productFrame1,text="Note: Enter 0 QTY to remove product from the cart",font=("cambria",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)
        
        #--------------------Customer Frame---------------
        self.var_cname = StringVar()
        self.var_contact = StringVar()
        CustomerFrame = Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=530,height=70)
        
        cTitle = Label(CustomerFrame,text="Customer Details",font=("cambria",15),bg="lightgray").pack(side=TOP,fill=X)
        lbl_name = Label(CustomerFrame,text="Name",font=("cambria",15),bg="white").place(x=5,y=35)
        txt_name = Entry(CustomerFrame,textvariable=self.var_cname,font=("cambria",13),bg="lightyellow").place(x=80,y=35,width=175)
        lbl_contact = Label(CustomerFrame,text="Contact",font=("cambria",15),bg="white").place(x=270,y=35)
        txt_contact = Entry(CustomerFrame,textvariable=self.var_contact,font=("cambria",13),bg="lightyellow").place(x=345,y=35,width=175)
        
        #---------------------------CAL CART FRAME---------------
        Cal_cart_Frame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cal_cart_Frame.place(x=420,y=190,width=530,height=360)
        
        #------------------CAL FRAME
        self.var_cal_input= StringVar()
        Cal_Frame = Frame(Cal_cart_Frame,bd=9,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=268,height=340)

        txt_cal_input = Entry(Cal_Frame,textvariable=self.var_cal_input,font=("arial",15,"bold"),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)
        
        btn_7 = Button(Cal_Frame,text=7,font=("arial",15,"bold"),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=0)
        btn_8 = Button(Cal_Frame,text=8,font=("arial",15,"bold"),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=1)
        btn_9 = Button(Cal_Frame,text=9,font=("arial",15,"bold"),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=2)
        btn_sum = Button(Cal_Frame,text='+',font=("arial",15,"bold"),command=lambda:self.get_input('+'),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=3)
        
        btn_4 = Button(Cal_Frame,text=4,font=("arial",15,"bold"),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=0)
        btn_5 = Button(Cal_Frame,text=5,font=("arial",15,"bold"),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=1)
        btn_6 = Button(Cal_Frame,text=6,font=("arial",15,"bold"),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=2)
        btn_subtract = Button(Cal_Frame,text='-',font=("arial",15,"bold"),command=lambda:self.get_input('-'),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=3)
        
        btn_1 = Button(Cal_Frame,text=1,font=("arial",15,"bold"),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=0)
        btn_2 = Button(Cal_Frame,text=2,font=("arial",15,"bold"),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=1)
        btn_3 = Button(Cal_Frame,text=3,font=("arial",15,"bold"),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=2)
        btn_multiply = Button(Cal_Frame,text='x',font=("arial",15,"bold"),command=lambda:self.get_input('x'),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=3)
        
        btn_0 = Button(Cal_Frame,text=0,font=("arial",15,"bold"),command=lambda:self.get_input(0),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=0)
        btn_c = Button(Cal_Frame,text='C',font=("arial",15,"bold"),command=self.clear_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=1)
        btn_eq = Button(Cal_Frame,text='=',font=("arial",15,"bold"),command=self.perform_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=2)
        btn_div = Button(Cal_Frame,text='/',font=("arial",15,"bold"),command=lambda:self.get_input('/'),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=3)


        #--------------CART FRAME
        CartFrame = Frame(Cal_cart_Frame,bd=3,relief=RIDGE)
        CartFrame.place(x=280,y=8,width=245,height=342)
        
        scrolly = Scrollbar(CartFrame,orient=VERTICAL)
        scrollx = Scrollbar(CartFrame,orient=HORIZONTAL)
        
        self.CartTable = ttk.Treeview(CartFrame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)
        
        self.CartTable.heading("pid",text="P ID")
        self.CartTable.heading("name",text="NAME")
        self.CartTable.heading("price",text="PRICE")
        self.CartTable.heading("qty",text="QTY")
        self.CartTable.heading("status",text="Status")

        self.CartTable["show"]="headings"
        
        self.CartTable.column("pid",width=40)
        self.CartTable.column("name",width=100)
        self.CartTable.column("price",width=90)
        self.CartTable.column("qty",width=40)
        self.CartTable.column("status",width=90)
        self.CartTable.pack(fill=BOTH,expand=1)
        #self.CartTable.bind("<ButtonRelease-1>",self.get_data)
        
        #------------------------------ADD CART Widgets Frame
        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()
        
        
        Add_CartWidgetsFrame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Add_CartWidgetsFrame.place(x=420,y=550,width=530,height=110)
        
        lbl_p_name = Label(Add_CartWidgetsFrame,text="Product Name",font=("cambria",15),bg="white").place(x=5,y=5)
        txt_p_name = Entry(Add_CartWidgetsFrame,textvariable=self.var_pname,font=("cambria",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)
        
        lbl_p_price = Label(Add_CartWidgetsFrame,text="Price Per Qty",font=("cambria",15),bg="white").place(x=230,y=5)
        txt_p_price = Entry(Add_CartWidgetsFrame,textvariable=self.var_price,font=("cambria",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)
        
        lbl_p_qty = Label(Add_CartWidgetsFrame,text="Qty",font=("cambria",15),bg="white").place(x=390,y=5)
        txt_p_qty = Entry(Add_CartWidgetsFrame,textvariable=self.var_qty,font=("cambria",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)
        
        self.lbl_inStock = Label(Add_CartWidgetsFrame,text="In Stock[9999]",font=("cambria",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)
               
        btn_clear_cart = Button(Add_CartWidgetsFrame,text="Clear",font=("cambria",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart = Button(Add_CartWidgetsFrame,text="Add | Update Cart",font=("cambria",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)
        
        #------------------------Billing Area----------------------------
        
        billFrame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billFrame.place(x=953,y=110,width=410,height=410)
        
        bTitle = Label(billFrame,text="Customer Bill",font=("cambria",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_bill_area = Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)
        
        #---------------------------------Billing Buttons---------------------
        billMenuFrame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billMenuFrame.place(x=953,y=520,width=410,height=140)
        
        self.lbl_amnt = Label(billMenuFrame,text="Bill Amount\n[0]",font=("cambria",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amnt.place(x=2,y=5,width=120,height=70)
        self.lbl_discount = Label(billMenuFrame,text="Discount\n[5%]",font=("cambria",15,"bold"),bg="#8bc34a",fg="white")
        self.lbl_discount.place(x=124,y=5,width=120,height=70)
        self.lbl_net_pay = Label(billMenuFrame,text="Net Pay\n[0]",font=("cambria",15,"bold"),bg="#607d8b",fg="white")
        self.lbl_net_pay.place(x=246,y=5,width=160,height=70)
        
        btn_print = Button(billMenuFrame,text="Print",cursor="hand2",font=("cambria",15,"bold"),bg="lightgreen",fg="white")
        btn_print.place(x=2,y=80,width=120,height=50)
        btn_clear_all = Button(billMenuFrame,text="Clear All",cursor="hand2",font=("cambria",15,"bold"),bg="gray",fg="white")
        btn_clear_all.place(x=124,y=80,width=120,height=50)
        btn_generate = Button(billMenuFrame,text="Generate/Save",cursor="hand2",font=("cambria",15,"bold"),bg="#009688",fg="white")
        btn_generate.place(x=246,y=80,width=160,height=50)
        
        
        #-------------------------Footer---------------------------
        footer = Label(self.root,text="IMS-Inventory Management System | Developed by Ayush & Swagat\nFor any technical issue contact:xxxxxxxxxx",font=("cambria",11),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        
        
        
    #--------------------------ALL FUNCTIONS--------------
    
    def get_input(self,num):
        xnum = self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
    
    def clear_cal(self):
        self.var_cal_input.set("")
    
    def perform_cal(self):
        result = self.var_cal_input.get()
        self.var_cal_input.set(eval(result))
    

if __name__=="__main__":
    root = Tk()
    obj = billClass(root)
    root.mainloop()