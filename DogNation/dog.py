#dog details
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox


class dog_details:
    def __init__(self, root):
        self.root = root
        self.root.title("DogNation")
        # Put frame geometry starting from 0, 0
        self.root.geometry("1295x550+0+0")

        ############### Variables#########
        self.var_dog_ID= StringVar()
        self.var_user_id=StringVar()
        self.var_gender=StringVar()
        self.var_liking=StringVar()
        self.var_breed_name=StringVar()
        self.var_weight=StringVar()
        self.var_adoption=StringVar()
        self.var_neuter_status=StringVar()
        self.var_dna_test=StringVar()
        self.var_special_needs=StringVar()
        self.var_age=StringVar()      


        # Title
        lbl1 = Label(self.root, text="ADD DOG DETAILS", font=("Arial", 18, "bold"), bg="black",
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
        lableframeleft = LabelFrame(self.root, bg="black",bd=2, relief=RIDGE, text="DOG DETAILS", padx=2, font=("Arial", 12, "bold"),fg="white")
        lableframeleft.place(x=5, y=50, width=425, height=620)

        # Dog details
        # dogID
        lbl_dog_id = Label(lableframeleft,bg="black", fg="white",text="Dog ID : ", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_dog_id.grid(row=0, column=0, sticky=W)
        entry_dog_id = ttk.Entry(lableframeleft, width=25,textvariable=self.var_dog_ID, font=("Arial", 11, "bold"))
        entry_dog_id.grid(row=0, column=1)

        #UserID
        lbl_dog_user_id = Label(lableframeleft,bg="black", fg="white", text="Owner ID : ", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_dog_user_id.grid(row=1, column=0, sticky=W)
        entry_dog_user_id = ttk.Entry(lableframeleft, width=25,state="readonly",textvariable=self.var_user_id, font=("Arial", 11, "bold"))
        entry_dog_user_id.grid(row=1, column=1)

        #Gender
        lbl_dog_gender = Label(lableframeleft,bg="black", fg="white", text="Gender : ", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_dog_gender.grid(row=2, column=0, sticky=W)
        entry_dog_gender= ttk.Entry(lableframeleft, width=25,textvariable=self.var_gender, font=("Arial", 11, "bold"))
        entry_dog_gender.grid(row=2, column=1)

        #Breed Name
        lbl_dog_breed_name = Label(lableframeleft,bg="black", fg="white", text="Breed Name : ", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_dog_breed_name.grid(row=3, column=0, sticky=W)
        entry_dog_breed_name = ttk.Entry(lableframeleft, width=25,textvariable=self.var_breed_name,font=("Arial", 11, "bold"))
        entry_dog_breed_name.grid(row=3, column=1)        
        
        #Weight
        lbl_dog_weight = Label(lableframeleft,bg="black", fg="white", text="Weight: ", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_dog_weight.grid(row=4, column=0, sticky=W)
        entry_dog_weight = ttk.Entry(lableframeleft, width=25,textvariable=self.var_weight, font=("Arial", 11, "bold"))
        entry_dog_weight.grid(row=4, column=1)

        #Liking
        lbl_dog_liking = Label(lableframeleft,bg="black", fg="white", text="Liking : ", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_dog_liking.grid(row=5, column=0, sticky=W)
        entry_dog_liking = ttk.Entry(lableframeleft, width=25,textvariable=self.var_liking,font=("Arial", 11, "bold"))
        entry_dog_liking.grid(row=5, column=1)

        #Adoption
        lbl_dog_adoption = Label(lableframeleft,bg="black", fg="white", text="Adoption : ", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_dog_adoption.grid(row=6, column=0, sticky=W)
        entry_dog_adoption = ttk.Entry(lableframeleft, width=25,textvariable=self.var_adoption,font=("Arial", 11, "bold"))
        entry_dog_adoption.grid(row=6, column=1)

        #Neuter Status
        lbl_dog_neuter_status = Label(lableframeleft,bg="black", fg="white",text="Neuter Status : ", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_dog_neuter_status .grid(row=7, column=0, sticky=W)
        entry_dog_neuter_status  = ttk.Entry(lableframeleft, width=25,textvariable=self.var_neuter_status,font=("Arial", 11, "bold"))
        entry_dog_neuter_status.grid(row=7, column=1)

        #DNA Test
        lbl_dog_dna_test = Label(lableframeleft, bg="black", fg="white",text="DNA Test : ", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_dog_dna_test.grid(row=8, column=0, sticky=W)
        combo_dog_dna_test = ttk.Combobox(lableframeleft,textvariable=self.var_dna_test, font=("Arial", 11, "bold"), width=23, state="readonly")
        combo_dog_dna_test["value"] = ("0", "1")
        combo_dog_dna_test.current(0)
        combo_dog_dna_test.grid(row=8, column=1)

        #Special Needs
        lbl_dog_special_needs = Label(lableframeleft,bg="black", fg="white", text="Special Needs : ", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_dog_special_needs.grid(row=9, column=0, sticky=W)
        entry_dog_special_needs = ttk.Entry(lableframeleft, width=25,textvariable=self.var_special_needs, font=("Arial", 11, "bold"))
        entry_dog_special_needs.grid(row=9, column=1)

        #Age
        lbl_dog_age = Label(lableframeleft,bg="black", fg="white", text="Age : ", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_dog_age.grid(row=10, column=0, sticky=W)
        entry_dog_age = ttk.Entry(lableframeleft, width=25,textvariable=self.var_age,font=("Arial", 11, "bold"))
        entry_dog_age.grid(row=10, column=1)

        # Buttons
        btn_frame = Frame(lableframeleft, bd=2,bg="black", relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=80)

        btnAdd = Button(btn_frame, text="ADD DOG",command= self.add_dogdata,font=("Arial", 9, "bold"),bg="orange", fg="white", width=9, padx=1)
        btnAdd.grid(row=0, column=0)

        btnAdd = Button(btn_frame, text="ADD DOG HEALTH",command= self.add_doghealthdata,font=("Arial", 9, "bold"), bg="orange", fg="white", width=17, padx=1)
        btnAdd.grid(row=0, column=1)

        btnUpdate = Button(btn_frame, text="UPDATE",command=self.update, font=("Arial", 9, "bold"), bg="orange", fg="white", width=9,
                        padx=1)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(btn_frame, text="DELETE",command=self.mDelete, font=("Arial", 9, "bold"), bg="orange", fg="white", width=9,
                        padx=1)
        btnDelete.grid(row=0, column=3)

        btnReset = Button(btn_frame, text="RESET",command=self.reset, font=("Arial", 9, "bold"), bg="orange", fg="white", width=9,
                        padx=1)
        btnReset.grid(row=0, column=4)

        # Table Frame search system
        TableFrame = LabelFrame(self.root, bd=2, relief=RIDGE, text="VIEW DETAILS AND SEARCH SYSTEM", padx=2,
                                    font=("Arial", 12, "bold"))
        TableFrame.place(x=435, y=50, width=860, height=490)

        lbl_searchby = Label(TableFrame, text="Search By : ", font=("Arial", 12, "bold"), bg="orange", fg="white")
        lbl_searchby.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var=StringVar()
        combo_search = ttk.Combobox(TableFrame,textvariable=self.search_var,font=("Arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("dog.dog_id", "user_id")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search=StringVar()
        entry_dog_search = ttk.Entry(TableFrame,textvariable=self.txt_search, width=24, font=("Arial", 13, "bold"))
        entry_dog_search.grid(row=0, column=2, padx=2)

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

        self.dog_details_Table = ttk.Treeview(DetailsFrame, column=("dog_ID", "user_id", "gender", "breed_name", "weight", "liking", "adoption", "neuter_status" , "dna_test", "special_needs", "age"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.dog_details_Table.xview)
        scroll_y.config(command=self.dog_details_Table.yview)

        self.dog_details_Table.heading("dog_ID", text="Dog ID")
        self.dog_details_Table.heading("user_id", text="Owner ID")
        self.dog_details_Table.heading("gender", text="Gender")
        self.dog_details_Table.heading("breed_name", text="Breed Name")
        self.dog_details_Table.heading("weight", text="Weight")
        self.dog_details_Table.heading("liking", text="Liking")
        self.dog_details_Table.heading("adoption", text="Adoption")
        self.dog_details_Table.heading("neuter_status", text="Neuter Status")
        self.dog_details_Table.heading("dna_test", text="DNA Test")
        self.dog_details_Table.heading("special_needs", text="Special Needs")
        self.dog_details_Table.heading("age", text="Age")

        self.dog_details_Table["show"] = "headings"
        self.dog_details_Table.column("dog_ID", width=100)
        self.dog_details_Table.column("user_id", width=100)
        self.dog_details_Table.column("gender", width=100)
        self.dog_details_Table.column("breed_name", width=100)
        self.dog_details_Table.column("weight", width=100)
        self.dog_details_Table.column("liking", width=100)
        self.dog_details_Table.column("adoption", width=100)
        self.dog_details_Table.column("neuter_status", width=100)
        self.dog_details_Table.column("special_needs", width=100)
        self.dog_details_Table.column("age", width=100)

        self.dog_details_Table.pack(fill=BOTH, expand=1)
        self.dog_details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_dogdata(self):
        if self.var_liking.get()=="":
            messagebox.showerror("Error","All details are required",parent=self.root)  
        else :
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
                my_cursor=conn.cursor()
                my_cursor.execute("insert into dog values(%s,Null,%s,%s,%s,%s,%s)",(
                                                                        self.var_dog_ID.get(),
                                                                        #self.var_user_id.get(),
                                                                        self.var_gender.get(),                                                                        
                                                                        self.var_breed_name.get(),
                                                                        self.var_weight.get(),
                                                                        self.var_liking.get(),
                                                                        self.var_adoption.get()                                                      
                                                                    ))
                conn.commit()
                self.fetch_data
                conn.close()
                messagebox.showinfo("Success", "Dog has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong :{str(es)}",parent=self.root)

    def add_doghealthdata(self):
        if self.var_dog_ID.get()=="":
            messagebox.showerror("Error","All details are required",parent=self.root)  
        else :
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
                my_cursor=conn.cursor()
                my_cursor.execute("insert into health values(%s,%s,%s,%s,%s)",(
                                                                        self.var_dog_ID.get(),
                                                                        self.var_neuter_status.get(),
                                                                        self.var_dna_test.get(),
                                                                        self.var_special_needs.get(),
                                                                        self.var_age.get() 
                                                                    ))
                conn.commit()
                self.fetch_data
                conn.close()
                messagebox.showinfo("Success", "Dog has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong :{str(es)}",parent=self.root)
              
    """ def fetch_tabledata(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
        my_cursor=conn.cursor()
        my_cursor.execute("select dog.dog_id,user_id,gender,breed_name,weight,neuter_status,special_needs,age from dog,health where dog.dog_id = health.dog_id")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.dog_details_Table.delete(*self.dog_details_Table.get_children())
            for i in rows :
                self.dog_details_Table.insert("",END,values=i)
            conn.commit()
        conn.close() """

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
        my_cursor=conn.cursor()
        my_cursor.execute("select dog.dog_id,user_id,gender,breed_name,weight,liking,adoption,neuter_status,dna_test,special_needs,age from dog,health where dog.dog_id = health.dog_id")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.dog_details_Table.delete(*self.dog_details_Table.get_children())
            for i in rows :
                self.dog_details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,events=""):
        cursor_row=self.dog_details_Table.focus()
        content=self.dog_details_Table.item(cursor_row)
        row=content["values"]

        self.var_dog_ID.set(row[0])
        self.var_user_id.set(row[1])
        self.var_gender.set(row[2])
        self.var_breed_name.set(row[3])
        self.var_weight.set(row[4])
        self.var_liking.set(row[5])
        self.var_adoption.set(row[6])
        self.var_neuter_status.set(row[7])
        self.var_dna_test.set(row[8])
        self.var_special_needs.set(row[9])
        self.var_age.set(row[10])
     
    def update (self):
        if self.var_dog_ID.get()=="":
            messagebox.showerror("Error","please enter the dog ID",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
            my_cursor=conn.cursor()
            
            my_cursor.execute("update dog set gender = %s,breed_name = %s,weight = %s,liking= %s,adoption = %s where dog_id = %s",(                                                                                                                        
                                                                                                                        
                                                                                                                        self.var_gender.get(),                                                                                                                        
                                                                                                                        self.var_breed_name.get(),
                                                                                                                        self.var_weight.get(),
                                                                                                                        self.var_liking.get(),                                                                                                                        
                                                                                                                        self.var_adoption.get(),
                                                                                                                        self.var_dog_ID.get()
                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()

            conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
            my_cursor=conn.cursor()                       
            my_cursor.execute("update health set neuter_status = %s,dna_test = %s,special_needs= %s,age = %s where dog_id = %s",(                                                                                                                         
                                                                                                                        self.var_neuter_status.get(),
                                                                                                                        self.var_dna_test.get(),
                                                                                                                        self.var_special_needs.get(),
                                                                                                                        self.var_age.get(),
                                                                                                                        self.var_dog_ID.get()
                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Dog details have been updated successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("DogNation","Do you want to delete this dog",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
            my_cursor=conn.cursor()
            query ="delete from dog where dog_id=%s;"
            value=(self.var_user_ID.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data
        conn.close() 

    def reset(self):
        self.var_dog_ID.set(""),
        self.var_user_id.set(""),
        self.var_gender.set(""),
        self.var_breed_name.set(""),
        self.var_weight.set(""),
        self.var_liking.set(""),
        self.var_adoption.set(""),
        self.var_neuter_status.set(""),
        self.var_dna_test.set(""),
        self.var_special_needs.set("")
        self.var_age.set("")        
    
    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="yashmysql21",database="dognation") 
        my_cursor=conn.cursor()
       
        p = str(self.search_var.get())
        if p == "dog.dog_id":
            my_cursor.execute("select dog.dog_id,user_id,gender,breed_name,weight,liking,adoption,neuter_status,dna_test,special_needs,age from dog,health where dog.dog_id = health.dog_id AND "+str(self.search_var.get())+" like '%"+str(self.txt_search.get())+"%'")
            #my_cursor.execute("select dog.dog_id,user_id,gender,liking,breed_name,weight,adoption,neuter_status,dna_test,special_needs,age from dog,health where dog.dog_id = health.dog_id AND`" 
            #+"dog.dog_id"+"` like '%"+str(self.txt_search.get())+"%'")
        
        else:
            my_cursor.execute("select dog.dog_id,user_id,gender,breed_name,weight,liking,adoption,neuter_status,dna_test,special_needs,age from dog,health where dog.dog_id = health.dog_id AND "+str(self.search_var.get())+" like '%"+str(self.txt_search.get())+"%'")  
           
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.dog_details_Table.delete(*self.dog_details_Table.get_children())
            for i in rows:
                self.dog_details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = dog_details(root)
    root.mainloop()