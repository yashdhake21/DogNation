#user details
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
import datetime


class user_details:
    def __init__(self, root):
        self.root = root
        self.root.title("DogNation")
        # Put frame geometry starting from 0, 0
        self.root.geometry("1295x600+0+0")

        ############### Variables#########
        self.var_user_ID= StringVar()
        #x= random.randint(1000,9999)
        self.var_user_ID.set(str())
        self.var_email_id=StringVar()
        self.var_name=StringVar()
        self.var_phone_number=IntVar()
        self.var_liking=IntVar()
        self.var_breed_want=StringVar()
        self.var_membership_type=IntVar()
        self.var_location_id=IntVar()
        self.var_max_dog_age=IntVar()
        self.var_last_active=StringVar()
        self.var_mem_end=StringVar()
        self.var_payment_status=StringVar()        


        # Title
        lbl1 = Label(self.root, text="ADD USER DETAILS", font=("Arial", 18, "bold"), bg="black",
                     fg="orange", bd=7, relief=RIDGE)
        lbl1.place(x=0, y=0, width=1295, height=50)

        # Logo
        img1 = Image.open("5.png")
        img1 = img1.resize((100, 30), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl2 = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE)
        lbl2.place(x=5, y=8, width=100, height=30)

        # Label Frame
        lableframeleft = LabelFrame(self.root, bg="black",bd=2, relief=RIDGE, text="USER DETAILS", padx=2, font=("Arial", 12, "bold"), fg="white")
        lableframeleft.place(x=5, y=50, width=425, height=720)

        # User details
        # userID
        lbl_user_id = Label(lableframeleft, bg="black",text="User ID : ", font=("Arial", 12, "bold"),fg="white", pady=6)
        lbl_user_id.grid(row=0, column=0, sticky=W)
        entry_user_id = ttk.Entry(lableframeleft, width=25,textvariable=self.var_user_ID, font=("Arial", 11, "bold"))
        entry_user_id.grid(row=0, column=1)

        # Email
        lbl_user_email = Label(lableframeleft,bg="black", text="Email ID : ", font=("Arial", 12, "bold"),fg="white", padx=2, pady=6)
        lbl_user_email.grid(row=1, column=0, sticky=W)
        entry_user_email = ttk.Entry(lableframeleft, width=25,textvariable=self.var_email_id, font=("Arial", 11, "bold"))
        entry_user_email.grid(row=1, column=1)

        #Name
        lbl_user_name = Label(lableframeleft,bg="black", text="Name : ", font=("Arial", 12, "bold"),fg="white", padx=2, pady=6)
        lbl_user_name.grid(row=2, column=0, sticky=W)
        entry_user_name = ttk.Entry(lableframeleft, width=25,textvariable=self.var_name, font=("Arial", 11, "bold"))
        entry_user_name.grid(row=2, column=1)

        #MobileNo:
        lbl_user_phone_number = Label(lableframeleft,bg="black", text="Phone Number : ", font=("Arial", 12, "bold"),fg="white", padx=2, pady=6)
        lbl_user_phone_number.grid(row=3, column=0, sticky=W)
        entry_user_phone_number = ttk.Entry(lableframeleft, width=25,textvariable=self.var_phone_number,font=("Arial", 11, "bold"))
        entry_user_phone_number.grid(row=3, column=1)

        #Likings:
        lbl_user_liking = Label(lableframeleft,bg="black", text="Likings : ", font=("Arial", 12, "bold"), fg="white",padx=2, pady=6)
        lbl_user_liking.grid(row=4, column=0, sticky=W)
        entry_user_liking = ttk.Entry(lableframeleft, width=25,textvariable=self.var_liking,font=("Arial", 11, "bold"))
        entry_user_liking.grid(row=4, column=1)

        #Breed Want
        lbl_user_breed_want = Label(lableframeleft,bg="black", text="Breed Want : ", font=("Arial", 12, "bold"),fg="white", padx=2, pady=6)
        lbl_user_breed_want.grid(row=5, column=0, sticky=W)
        entry_user_breed_want = ttk.Entry(lableframeleft, width=25,textvariable=self.var_breed_want, font=("Arial", 11, "bold"))
        entry_user_breed_want.grid(row=5, column=1)

        #Location ID:
        lbl_user_location_id = Label(lableframeleft,bg="black", text="Location ID : ", font=("Arial", 12, "bold"),fg="white", padx=2, pady=6)
        lbl_user_location_id.grid(row=6, column=0, sticky=W)
        entry_user_location_id = ttk.Entry(lableframeleft, width=25,textvariable=self.var_location_id,font=("Arial", 11, "bold"))
        entry_user_location_id.grid(row=6, column=1)

        #Max Dog Age
        lbl_user_max_dog_age = Label(lableframeleft,bg="black", text="Max Dog Age : ", font=("Arial", 12, "bold"),fg="white", padx=2, pady=6)
        lbl_user_max_dog_age.grid(row=7, column=0, sticky=W)
        entry_user_max_dog_age = ttk.Entry(lableframeleft, width=25,textvariable=self.var_max_dog_age,font=("Arial", 11, "bold"))
        entry_user_max_dog_age.grid(row=7, column=1)

        # Membership Type
        lbl_user_membership_type = Label(lableframeleft,bg="black", text="Membership Type : ", font=("Arial", 12, "bold"),fg="white", padx=2, pady=6)
        lbl_user_membership_type.grid(row=8, column=0, sticky=W)
        combo_user_membership_type = ttk.Combobox(lableframeleft,textvariable=self.var_membership_type, font=("Arial", 11, "bold"), width=23, state="readonly")
        combo_user_membership_type["value"] = ("0", "1", "2")
        combo_user_membership_type.current(0)
        combo_user_membership_type.grid(row=8, column=1)

        #Last Active
        lbl_user_last_active = Label(lableframeleft,bg="black",text="Last Active: ", font=("Arial", 12, "bold"), fg="white",padx=2, pady=6)
        lbl_user_last_active.grid(row=9, column=0, sticky=W)
        entry_user_last_active= ttk.Entry(lableframeleft, width=25,textvariable=self.var_last_active, font=("Arial", 11, "bold"))
        entry_user_last_active.grid(row=9, column=1)

        # Membership End
        lbl_user_membership_end = Label(lableframeleft,bg="black", text="Membership End: ", font=("Arial", 12, "bold"),fg="white", padx=2, pady=6)
        lbl_user_membership_end.grid(row=10, column=0, sticky=W)
        entry_user_membership_end = ttk.Entry(lableframeleft, width=25,textvariable=self.var_mem_end, font=("Arial", 11, "bold"))
        entry_user_membership_end.grid(row=10, column=1)

        # Payment Status
        lbl_user_payment_status = Label(lableframeleft,bg="black", text="Payment Status: ", font=("Arial", 12, "bold"),fg="white", padx=2, pady=6)
        lbl_user_payment_status.grid(row=11, column=0, sticky=W)
        entry_user_payment_status= ttk.Entry(lableframeleft, width=25,textvariable=self.var_payment_status, font=("Arial", 11, "bold"))
        entry_user_payment_status.grid(row=11, column=1)

        # Buttons
        btn_frame = Frame(lableframeleft, bg="black", relief=RIDGE)
        btn_frame.place(x=0, y=430, width=412, height=80)

        btnAdd = Button(btn_frame, text="ADD",command= self.add_userdata,font=("Arial", 12, "bold"), bg="orange", fg="white", width=10, padx=5)
        btnAdd.grid(row=0, column=0)

        # btnAdd = Button(btn_frame, text="Add User Membership",command= self.add_membershipdata,font=("Arial", 8, "bold"), bg="black", fg="gold", width=14, padx=1)
        # btnAdd.grid(row=1, column=0)

        btnUpdate = Button(btn_frame, text="UPDATE",command=self.update, font=("Arial", 12, "bold"), bg="orange", fg="white", width=10,
                        padx=5)
        btnUpdate.grid(row=0, column=1)

        btnDelete = Button(btn_frame, text="DELETE",command=self.mDelete, font=("Arial", 12, "bold"), bg="orange", fg="white", width=10,
                        padx=5)
        btnDelete.grid(row=0, column=2)

        btnReset = Button(btn_frame, text="RESET",command=self.reset, font=("Arial", 12, "bold"), bg="orange", fg="white", width=10,
                        padx=5)
        btnReset.grid(row=0, column=3)

        # Table Frame search system
        TableFrame = LabelFrame(self.root, bd=2, relief=RIDGE, text="VIEW DETAILS AND SEARCH SYSTEM", padx=2,
                                    font=("Arial", 12, "bold"))
        TableFrame.place(x=435, y=50, width=860, height=530)

        lbl_searchby = Label(TableFrame, text="Search By : ", font=("Arial", 12, "bold"), bg="orange", fg="white")
        lbl_searchby.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var=StringVar()
        combo_search = ttk.Combobox(TableFrame,textvariable=self.search_var,font=("Arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("email_id", "Name")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search=StringVar()
        entry_user_search = ttk.Entry(TableFrame,textvariable=self.txt_search, width=24, font=("Arial", 13, "bold"))
        entry_user_search.grid(row=0, column=2, padx=2)

        btnSearch = Button(TableFrame, text="SEARCH",command=self.search, font=("Arial", 12, "bold"), bg="black", fg="gold",
                          width=10, padx=1, bd=2)
        btnSearch.grid(row=0, column=3, padx=2)

        btnShowAll = Button(TableFrame, text="SHOW ALL",command=self.fetch_data, font=("Arial", 12, "bold"), bg="black", fg="gold",
                          width=10, padx=1, bd=2)
        btnShowAll.grid(row=0, column=4, padx=2)

        # Show Data Table
        DetailsFrame = Frame(TableFrame, bd=2, relief=RIDGE)
        DetailsFrame.place(x=0, y=50, width=830, height=450)

        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)

        self.user_details_table = ttk.Treeview(DetailsFrame, column=("ID","Em","Name","mob","liking","breed_want","location_id","max_dog_age","mem_type","last_active","mem_end","payment_status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.user_details_table.xview)
        scroll_y.config(command=self.user_details_table.yview)

        self.user_details_table.heading("ID", text="User ID")
        self.user_details_table.heading("Em", text="Email")
        self.user_details_table.heading("Name", text="Customer Name")
        self.user_details_table.heading("mob", text="Mobile No")
        self.user_details_table.heading("liking", text="Liking")
        self.user_details_table.heading("breed_want", text="Breed Choice")
        self.user_details_table.heading("location_id", text="Location ID")
        self.user_details_table.heading("max_dog_age", text="Max Dog Age")
        self.user_details_table.heading("mem_type", text="Membership Type")
        self.user_details_table.heading("last_active", text="Last Active")
        self.user_details_table.heading("mem_end", text="Membership End")
        self.user_details_table.heading("payment_status", text="Payment Status")

        self.user_details_table["show"] = "headings"
        self.user_details_table.column("ID", width=100)
        self.user_details_table.column("Em", width=100)
        self.user_details_table.column("Name", width=100)
        self.user_details_table.column("mob", width=100)
        self.user_details_table.column("liking", width=100)
        self.user_details_table.column("breed_want", width=100)
        self.user_details_table.column("location_id", width=100)
        self.user_details_table.column("max_dog_age", width=100)
        self.user_details_table.column("mem_type", width=100)
        self.user_details_table.column("last_active", width=100)
        self.user_details_table.column("mem_end", width=100)
        self.user_details_table.column("payment_status", width=100)

        self.user_details_table.pack(fill=BOTH, expand=1)
        self.user_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_userdata(self):
        if self.var_phone_number.get()=="":
            messagebox.showerror("Error","All details are required",parent=self.root)  
        else :
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
                my_cursor=conn.cursor()
                my_cursor.execute("insert into users values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                        self.var_user_ID.get(),
                                                                        self.var_email_id.get(),
                                                                        self.var_name.get(),
                                                                        self.var_phone_number.get(),
                                                                        self.var_liking.get(),
                                                                        self.var_breed_want.get(),
                                                                        self.var_location_id.get(),
                                                                        self.var_max_dog_age.get(),                                                           
                                                                    ))
                conn.commit()
                self.fetch_data
                conn.close()

                conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
                my_cursor=conn.cursor()
                my_cursor.execute("insert into membership (user_id,membership_type,last_active,mem_end,payment_status) values(%s,%s,%s,%s,1)",(
                                                                        self.var_user_ID.get(),
                                                                        self.var_membership_type.get(),
                                                                        self.var_last_active.get(),
                                                                        self.var_mem_end.get()
                                                                        #self.var_payment_status.get()  
                                                                    ))
                conn.commit()
                self.fetch_data
                conn.close() 

                messagebox.showinfo("Success", "User has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong :{str(es)}",parent=self.root)

    # def add_membershipdata(self):
    #     if self.var_user_ID.get()=="":
    #         messagebox.showerror("Error","All details are required",parent=self.root)  
    #     else :
    #         try:
    #             conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
    #             my_cursor=conn.cursor()
    #             my_cursor.execute("insert into membership values(%s,%s,%s,%s,%s)",(
    #                                                                     self.var_user_ID.get(),
    #                                                                     self.var_membership_type.get(),
    #                                                                     self.var_last_active.get(),
    #                                                                     self.var_mem_end.get(),
    #                                                                     self.var_payment_status.get()  
    #                                                                 ))
    #             conn.commit()
    #             self.fetch_data
    #             conn.close()
    #             messagebox.showinfo("Success", "User Membership details have been added",parent=self.root)
    #         except Exception as es:
    #             messagebox.showwarning("warning",f"something went wrong :{str(es)}",parent=self.root)
              
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
        my_cursor=conn.cursor()
        my_cursor.execute("select users.user_id,email_id,name,phone_number,liking,breed_want,location_id,max_dog_age,membership_type,last_active,mem_end,payment_status from users,membership where users.user_id = membership.user_id;")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.user_details_table.delete(*self.user_details_table.get_children())
            for i in rows :
                self.user_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,events=""):
        cursor_row=self.user_details_table.focus()
        content=self.user_details_table.item(cursor_row)
        row=content["values"]

        self.var_user_ID.set(row[0])
        self.var_email_id.set(row[1])
        self.var_name.set(row[2])
        self.var_phone_number.set(row[3])
        self.var_liking.set(row[4])
        self.var_breed_want.set(row[5])
        self.var_location_id.set(row[6])
        self.var_max_dog_age.set(row[7])
        self.var_membership_type.set(row[8])
        self.var_last_active.set(row[9])
        self.var_mem_end.set(row[10])
        self.var_payment_status.set(row[11])
     
    def update (self):
        if self.var_phone_number.get()=="":
            messagebox.showerror("Error","please enter the number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
            my_cursor=conn.cursor()            
            my_cursor.execute("update users set email_id = %s,name = %s,phone_number= %s,liking = %s,breed_want = %s,location_id = %s, max_dog_age = %s  where user_id =(%s)",( 
                                                                                                                        #self.var_user_ID.get(),
                                                                                                                        self.var_email_id.get(),
                                                                                                                        self.var_name.get(),
                                                                                                                        self.var_phone_number.get(),
                                                                                                                        self.var_liking.get(),
                                                                                                                        self.var_breed_want.get(),                                                                                                                        
                                                                                                                        self.var_location_id.get(),
                                                                                                                        self.var_max_dog_age.get(),
                                                                                                                        self.var_user_ID.get(),
                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()

            conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
            my_cursor=conn.cursor()            
            my_cursor.execute("update membership set membership_type= %s,last_active= %s,mem_end= %s,payment_status= %s where user_id =(%s)",( 
                                                                                                                        self.var_membership_type.get(),
                                                                                                                        self.var_last_active.get(),
                                                                                                                        self.var_mem_end.get(),
                                                                                                                        self.var_payment_status.get(),
                                                                                                                        self.var_user_ID.get()
                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","User details have been updated successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("DogNation","Do you want to delete this user",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
            my_cursor=conn.cursor()
            query ="delete from users where user_id=%s;"
            value=(self.var_user_ID.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data
        conn.close() 

    def reset(self):
        self.var_user_ID.set(""),
        self.var_email_id.set(""),
        self.var_name.set(""),
        self.var_phone_number.set(""),
        self.var_liking.set(""),
        self.var_breed_want.set(""),
        self.var_membership_type.set(""),
        self.var_last_active.set(""),
        self.var_location_id.set(""),
        self.var_max_dog_age.set(""),
        self.var_mem_end.set("")
        self.var_payment_status.set("")        
    
    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
        my_cursor=conn.cursor()
       
        p = str(self.search_var.get())
        if p == "email_id":
            #my_cursor.execute("select * from dog where "+str(self.search_var.get())+" like '%"+str(self.txt_search.get())+"%'")
            my_cursor.execute("select users.user_id,email_id,name,phone_number,liking,breed_want,location_id,max_dog_age,membership_type,mem_end,payment_status from users,membership where users.user_id = membership.user_id AND`" 
            +str(self.search_var.get())+"` like '%"+str(self.txt_search.get())+"%'")
        else:
            my_cursor.execute("select users.user_id,email_id,name,phone_number,liking,breed_want,location_id,max_dog_age,membership_type,mem_end,payment_status from users,membership where users.user_id = membership.user_id AND`"
            +str(self.search_var.get())+"` like '%"+str(self.txt_search.get())+"%'")        
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.user_details_table.delete(*self.user_details_table.get_children())
            for i in rows:
                self.user_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    """ def randomdate():
        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2021, 11, 1)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        return(random_date) """


if __name__ == "__main__":
    root = Tk()
    obj = user_details(root)
    root.mainloop()