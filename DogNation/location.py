#location details

from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox



class location_details:
    def __init__(self, root):
        self.root = root
        self.root.title("DogNation")
        self.root.geometry("1295x600+0+0")
        self.var_location_id=IntVar()
        self.var_zipcode=IntVar()
        self.var_city=StringVar()
        self.var_state=StringVar()
        self.var_country=StringVar()        


        # Title
        lbl1 = Label(self.root, text="LOCATION DETAILS", font=("Arial", 18, "bold"), bg="black",
                     fg="gold", bd=4, relief=RIDGE)
        lbl1.place(x=0, y=0, width=1295, height=50)

         # Logo
        img1 = Image.open("5.png")
        img1 = img1.resize((100, 30), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl2 = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE)
        lbl2.place(x=5, y=8, width=100, height=30)


        # Logo
        # img1 = Image.open("pic7.jfif")
        # img1 = img1.resize((100, 40), Image.ANTIALIAS)
        # self.photoimg1 = ImageTk.PhotoImage(img1)
        # lbl2 = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE)
        # lbl2.place(x=5, y=2, width=100, height=40)

        # Image
        """ img2 = Image.open("pic8.jfif")
        img2 = img2.resize((425, 100), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl3 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lbl3.place(x=5, y=530, width=425, height=100) """

        # Label Frame
        lableframeleft = LabelFrame(self.root, bg="black",fg="white",bd=2, relief=RIDGE, text="LOCATION DETAILS", padx=2, font=("Arial", 12, "bold"))
        lableframeleft.place(x=5, y=50, width=425, height=720)

        # Location Details
        # Location ID
        lbl_user_id = Label(lableframeleft, bg="black",fg="white",text="Location ID : ", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_user_id.grid(row=0, column=0, sticky=W)
        entry_user_id = ttk.Entry(lableframeleft, width=25,textvariable=self.var_location_id, font=("Arial", 11, "bold"))
        entry_user_id.grid(row=0, column=1)

        #Email
        lbl_user_zipcode = Label(lableframeleft,bg="black",fg="white", text="ZIPCODE : ", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_user_zipcode.grid(row=1, column=0, sticky=W)
        entry_user_zipcode = ttk.Entry(lableframeleft, width=25,textvariable=self.var_zipcode, font=("Arial", 11, "bold"))
        entry_user_zipcode.grid(row=1, column=1)

        #City
        lbl_user_city = Label(lableframeleft,bg="black",fg="white", text="City : ", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_user_city.grid(row=2, column=0, sticky=W)
        entry_user_city = ttk.Entry(lableframeleft, width=25,textvariable=self.var_city, font=("Arial", 11, "bold"))
        entry_user_city.grid(row=2, column=1)

        #State
        lbl_user_state = Label(lableframeleft,bg="black",fg="white", text="State : ", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_user_state.grid(row=3, column=0, sticky=W)
        entry_user_state = ttk.Entry(lableframeleft, width=25,textvariable=self.var_state,font=("Arial", 11, "bold"))
        entry_user_state.grid(row=3, column=1)

        #Country
        lbl_user_country = Label(lableframeleft, bg="black",fg="white",text="Country : ", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_user_country.grid(row=4, column=0, sticky=W)
        entry_user_country = ttk.Entry(lableframeleft, width=25,textvariable=self.var_country,font=("Arial", 11, "bold"))
        entry_user_country.grid(row=4, column=1)

        
        # Buttons
        btn_frame = Frame(lableframeleft, bg="black", relief=RIDGE)
        btn_frame.place(x=0, y=220, width=412, height=80)

        btnAdd = Button(btn_frame, text="ADD",command= self.add_locationdata,font=("Arial", 12, "bold"), bg="orange", fg="white", width=10, padx=1)
        btnAdd.grid(row=0, column=0)

        btnUpdate = Button(btn_frame, text="UPDATE",command=self.update, font=("Arial", 12, "bold"), bg="orange", fg="white", width=10,
                        padx=1)
        btnUpdate.grid(row=0, column=1)

        btnDelete = Button(btn_frame, text="DELETE",command=self.mDelete, font=("Arial", 12, "bold"), bg="orange", fg="white", width=10,
                        padx=1)
        btnDelete.grid(row=0, column=2)

        btnReset = Button(btn_frame, text="RESET",command=self.reset, font=("Arial", 12, "bold"), bg="orange", fg="white", width=10,
                        padx=1)
        btnReset.grid(row=0, column=3)

        # Table Frame search system
        TableFrame = LabelFrame(self.root, bd=2, relief=RIDGE, text="VIEW DETAILS AND SEARCH SYSTEM", padx=2,
                                    font=("Arial", 12, "bold"))
        TableFrame.place(x=435, y=50, width=860, height=490)

        lbl_searchby = Label(TableFrame, text="Search By : ", font=("Arial", 12, "bold"), bg="orange", fg="white")
        lbl_searchby.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var=StringVar()
        combo_search = ttk.Combobox(TableFrame,textvariable=self.search_var,font=("Arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("location_id", "zipcode")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search=StringVar()
        entry_location_search = ttk.Entry(TableFrame,textvariable=self.txt_search, width=24, font=("Arial", 13, "bold"))
        entry_location_search.grid(row=0, column=2, padx=2)

        btnSearch = Button(TableFrame, text="SEARCH",command=self.search, font=("Arial", 12, "bold"), bg="black", fg="orange",
                          width=10, padx=1)
        btnSearch.grid(row=0, column=3, padx=2)

        btnShowAll = Button(TableFrame, text="SHOW ALL",command=self.fetch_data, font=("Arial", 12, "bold"), bg="black", fg="orange",
                          width=10, padx=1)
        btnShowAll.grid(row=0, column=4, padx=2)

        # Show Data Table
        DetailsFrame = Frame(TableFrame, bd=2, relief=RIDGE)
        DetailsFrame.place(x=0, y=50, width=830, height=400)

        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)

        self.location_table = ttk.Treeview(DetailsFrame, column=("location_id","zipcode","city","state","country"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.location_table.xview)
        scroll_y.config(command=self.location_table.yview)

        self.location_table.heading("location_id", text="Location ID")
        self.location_table.heading("zipcode", text="Zipcode")
        self.location_table.heading("city", text="City")
        self.location_table.heading("state", text="State")
        self.location_table.heading("country", text="Country")

        self.location_table["show"] = "headings"
        self.location_table.column("location_id", width=100)
        self.location_table.column("zipcode", width=100)
        self.location_table.column("city", width=100)
        self.location_table.column("state", width=100)
        self.location_table.column("country", width=100)

        self.location_table.pack(fill=BOTH, expand=1)
        self.location_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_locationdata(self):
        if self.var_location_id.get()=="":
            messagebox.showerror("Error","All details are required",parent=self.root)  
        else :
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
                my_cursor=conn.cursor()
                my_cursor.execute("insert into location values(%s,%s,%s,%s,%s)",(
                                                                        self.var_location_id.get(),
                                                                        self.var_zipcode.get(),
                                                                        self.var_city.get(),
                                                                        self.var_state.get(),
                                                                        self.var_country.get()  
                                                                    ))
                conn.commit()
                self.fetch_data
                conn.close()
                messagebox.showinfo("Success", "New location details have been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong :{str(es)}",parent=self.root)
              
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
        my_cursor=conn.cursor()
        my_cursor.execute("select * from location")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.location_table.delete(*self.location_table.get_children())
            for i in rows :
                self.location_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,events=""):
        cursor_row=self.location_table.focus()
        content=self.location_table.item(cursor_row)
        row=content["values"]

        self.var_location_id.set(row[0])
        self.var_zipcode.set(row[1])
        self.var_city.set(row[2])
        self.var_state.set(row[3])
        self.var_country.set(row[4])

    def update (self):
        if self.var_location_id.get()=="":
            messagebox.showerror("Error","Please enter Location ID",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
            my_cursor=conn.cursor()            
            my_cursor.execute("update location set zipcode = %s,city = %s,state= %s,country= %s where location_id =(%s)",(                                                                                                                         
                                                                                                                        self.var_zipcode.get(),
                                                                                                                        self.var_city.get(),
                                                                                                                        self.var_state.get(),
                                                                                                                        self.var_country.get(),                                                                                                                      
                                                                                                                        self.var_location_id.get(),
                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","User details have been updated successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("DogNation","Do you want to delete this location",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
            my_cursor=conn.cursor()
            query ="delete from location where location_id=%s;"
            value=(self.var_location_id.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data
        conn.close() 

    def reset(self):
        self.var_location_id.set(""),
        self.var_zipcode.set(""),
        self.var_city.set(""),
        self.var_state.set(""),
        self.var_country.set(""),     
    
    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
        my_cursor=conn.cursor()
       
        p = str(self.search_var.get())
        if p == "location_id":
            #my_cursor.execute("select * from dog where "+str(self.search_var.get())+" like '%"+str(self.txt_search.get())+"%'")
            my_cursor.execute("select * from location where`" 
            +str(self.search_var.get())+"` like '%"+str(self.txt_search.get())+"%'")
        else:
            my_cursor.execute("select * from location where`"
            +str(self.search_var.get())+"` like '%"+str(self.txt_search.get())+"%'")        
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.location_table.delete(*self.location_table.get_children())
            for i in rows:
                self.location_table.insert("",END,values=i)
            conn.commit()
        conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = location_details(root)
    root.mainloop()