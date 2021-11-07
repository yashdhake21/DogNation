#Adopt a dog

from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class adopt_dog:
    def __init__(self, root):
        self.root = root
        self.root.title("DOGNATION")
        # Put frame geometry starting from 0, 0
        self.root.geometry("1295x550+0+0")
        # Variables      
        self.var_email_id = StringVar()
        self.var_dog_id = StringVar()
        self.var_gender = StringVar()
        self.var_breed_name = StringVar()
        self.var_weight = StringVar()
        self.var_neuter_status = StringVar()
        self.var_dna_test = StringVar()
        self.var_special_needs = StringVar()
        self.var_age = StringVar()
        self.var_adoption = StringVar()
        self.var_dogliking = StringVar()
        self.var_userliking = StringVar()
        self.var_user_id = StringVar()
        
        # Title

        lbl1 = Label(self.root, text="ADOPT DOG", font=("Arial", 18, "bold"), bg="black",
                     fg="gold", bd=4, relief=RIDGE)
        lbl1.place(x=0, y=0, width=1295, height=50)


         # Logo
        img1 = Image.open("5.png")
        img1 = img1.resize((100, 30), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl2 = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE)
        lbl2.place(x=5, y=8, width=100, height=30)

        # Label Frame
        lableframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="DOG DETAILS", padx=2,
                                    font=("Arial", 12, "bold"), bg="black", fg="white")
        lableframeleft.place(x=5, y=50, width=425, height=530)

        img1l = Image.open("26.jpg")
        img1l = img1l.resize((410,245), Image.ANTIALIAS)
        self.photoimg1l = ImageTk.PhotoImage(img1l)
        lbl2l = Label(lableframeleft, image=self.photoimg1l, bd=0, relief=RIDGE)
        lbl2l.place(x=5, y=200, width=410, height=245)
        

        #Adoptee Details
        #Email ID
        lbl_email_id = Label(lableframeleft, text="Email ID : ", font=("Arial", 11, "bold"), bg="black", fg="white", padx=2,
                            pady=12)
        lbl_email_id.grid(row=0, column=0, sticky=W)
        entry_email_id = ttk.Entry(lableframeleft, textvariable=self.var_email_id, width=25,
                                  font=("Arial", 13, "bold"))
        entry_email_id.grid(row=0, column=1, sticky=W)

        #Dog ID
        lbl_dog_id = Label(lableframeleft, text="Dog ID : ", font=("Arial", 11, "bold"),bg="black", fg="white", padx=2,
                            pady=12)
        lbl_dog_id.grid(row=1, column=0, sticky=W)
        entry_dog_id = ttk.Entry(lableframeleft, textvariable=self.var_dog_id, width=25,
                                  font=("Arial", 13, "bold"))
        entry_dog_id.grid(row=1, column=1)

        #Adoption Status
        lbl_adoption = Label(lableframeleft, text="Adoption Status : ", font=("Arial", 11, "bold"),bg="black", fg="white", padx=2,
                            pady=12)
        lbl_adoption.grid(row=2, column=0, sticky=W)
        entry_adoption = ttk.Entry(lableframeleft, textvariable=self.var_adoption, width=25,
                                  font=("Arial", 13, "bold"))
        entry_adoption.grid(row=2, column=1)

        # Buttons
        btn_frame = Frame(lableframeleft, bd=1,bg="black", relief=RIDGE)
        btn_frame.place(x=0, y=150, width=412, height=40)

        btnUpdate = Button(btn_frame, text="UPDATE", command=self.update, font=("Arial", 12, "bold"),
                           bg="orange", fg="white", width=12)
        btnUpdate.grid(row=0, column=1)

        btnDelete = Button(btn_frame, text="DELETE", command=self.mDelete, font=("Arial", 12, "bold"),
                            bg="orange", fg="white", width=12)
        btnDelete.grid(row=0, column=2)

        btnReset = Button(btn_frame, text="RESET", command=self.reset, font=("Arial", 12, "bold"), bg="orange",
                          fg="white", width=12)
        btnReset.grid(row=0, column=3)

        # Table Frame
        TableFrame = LabelFrame(self.root, bd=2, relief=RIDGE, text="VIEW DETAILS AND SEARCH SYSTEM", padx=2,
                                font=("Arial", 12, "bold"))
        TableFrame.place(x=435, y=10, width=860, height=530)

        img1n = Image.open("22.jpg")
        img1n = img1n.resize((435,245), Image.ANTIALIAS)
        self.photoimg1n = ImageTk.PhotoImage(img1n)
        lbl2n = Label(TableFrame, image=self.photoimg1n, bd=0, relief=RIDGE)
        lbl2n.place(x=5, y=240, width=435, height=245)

        img1o = Image.open("25.jpg")
        img1o = img1o.resize((420, 245), Image.ANTIALIAS)
        self.photoimg1o = ImageTk.PhotoImage(img1o)
        lbl2o = Label(TableFrame, image=self.photoimg1o, bd=0, relief=RIDGE)
        lbl2o.place(x=380, y=240, width=420, height=245) 

        lbl_searchby = Label(TableFrame, text="Search By : ", font=("Arial", 12, "bold"), bg="orange",
                             fg="white")
        lbl_searchby.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(TableFrame,textvariable=self.search_var,font=("Arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("email_id", "name")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        entry_adoptdog_search = ttk.Entry(TableFrame,textvariable=self.txt_search,width=24, font=("Arial", 13, "bold"))
        entry_adoptdog_search.grid(row=0, column=2, padx=2)

        btnSearch = Button(TableFrame, text="SEARCH", command=self.search, font=("Arial", 12, "bold"),
                           bg="black", fg="orange", width=10, padx=1)
        btnSearch.grid(row=0, column=3, padx=2)

        btnShowAll = Button(TableFrame, text="SHOW ALL", command=self.fetch_data, font=("Arial", 12, "bold"),
                            bg="black", fg="orange", width=10, padx=1)
        btnShowAll.grid(row=0, column=4, padx=2)

        # Show Data Table
        DetailsFrame = Frame(TableFrame, bd=2, relief=RIDGE)
        DetailsFrame.place(x=0, y=50, width=830, height=180)

        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)

        self.adoptdog = ttk.Treeview(DetailsFrame, column=("dog_id", "email_id", "breed_name", "gender", "weight", "neuter_status", "dna_test" , "special_needs", "age","adoption","userlik","doglik","user_id"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.adoptdog.xview)
        scroll_y.config(command=self.adoptdog.yview)

        self.adoptdog.heading("dog_id", text="Dog ID")
        self.adoptdog.heading("email_id", text="Email ID")
        self.adoptdog.heading("breed_name", text="Breed Name")
        self.adoptdog.heading("gender", text="Gender")
        self.adoptdog.heading("weight", text="Weight")
        self.adoptdog.heading("neuter_status", text="Neuter Status")
        self.adoptdog.heading("dna_test", text="DNA Test")
        self.adoptdog.heading("special_needs", text="Special Needs")
        self.adoptdog.heading("age", text="Age")
        self.adoptdog.heading("adoption", text="Adoption")
        self.adoptdog.heading("userlik", text="User Liking")
        self.adoptdog.heading("doglik", text="Dog Liking")
        self.adoptdog.heading("user_id", text="User ID")


        self.adoptdog["show"] = "headings"
        self.adoptdog.column("dog_id", width=100)
        self.adoptdog.column("email_id", width=100)
        self.adoptdog.column("breed_name", width=100)
        self.adoptdog.column("gender", width=100)
        self.adoptdog.column("weight", width=100)
        self.adoptdog.column("neuter_status", width=100)
        self.adoptdog.column("dna_test", width=100)
        self.adoptdog.column("special_needs", width=100)
        self.adoptdog.column("age", width=100)
        self.adoptdog.column("adoption", width=100)
        self.adoptdog.column("userlik", width=100)
        self.adoptdog.column("doglik", width=100)
        self.adoptdog.column("user_id", width=100)
        

        self.adoptdog.pack(fill=BOTH, expand=1)
        self.adoptdog.bind("<ButtonRelease-1>",self.get_cursor)
        #self.fetch_data() 

    def fetch_data(self):
            conn = mysql.connector.connect(host="localhost", user="root", password="yashmysql21", database="dognation")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT dog.dog_id,users.email_id,dog.breed_name,dog.gender,dog.weight,health.neuter_status,health.dna_test,health.special_needs,health.age,dog.adoption,users.liking,dog.liking,users.user_id from dog INNER JOIN health ON dog.dog_id=health.dog_id INNER JOIN users ON dog.liking=users.liking WHERE dog.adoption = 0;")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.adoptdog.delete(*self.adoptdog.get_children())
                for i in rows:
                    self.adoptdog.insert("", END, values=i)
                conn.commit()
            conn.close()

    def get_cursor(self, events=""):
        cursor_row = self.adoptdog.focus()
        content = self.adoptdog.item(cursor_row)
        row = content["values"]

        self.var_dog_id.set(row[0])
        self.var_email_id.set(row[1])
        self.var_breed_name.set(row[2])
        self.var_gender.set(row[3])
        self.var_weight.set(row[4])
        self.var_neuter_status.set(row[5])
        self.var_dna_test.set(row[6])
        self.var_special_needs.set(row[7])
        self.var_age.set(row[8])
        self.var_adoption.set(row[9])
        self.var_dogliking.set(row[10])
        self.var_userliking.set(row[11])
        self.var_user_id.set(row[12])

    # UPDATE Adoption Status
    def update(self):
        if self.var_email_id.get() == "":
            messagebox.showerror("Error", "please enter the Email ID", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="yashmysql21", database="dognation")
            my_cursor = conn.cursor()
            adoptupdate = "UPDATE dog SET dog.user_id = (select user_id from users where email_id = %(email_id)s),dog.adoption = %(adoption)s WHERE dog.dog_id = (%(dog_id)s)"
            my_cursor.execute(adoptupdate,{'email_id': self.var_email_id.get(),'adoption': self.var_adoption.get(),'dog_id': self.var_dog_id.get()})
               
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Adoptee details have been updated successfully", parent=self.root)

    def mDelete(self):
         mDelete = messagebox.askyesno("DOGNATION","Do you want to delete this adopted dog",parent=self.root)
    #     if mDelete > 0:
    #         conn = mysql.connector.connect(host="localhost", user="root", password="yashmysql21", database="dognation")
    #         my_cursor = conn.cursor()
    #         query = "delete from dog where dog_id=%s;"
    #         value = (self.var_dog_id.get(),)
    #         my_cursor.execute(query, value)
    #     else:
    #         if not mDelete:
    #             return
    #     conn.commit()
    #     self.fetch_data
    #     conn.close()

    def reset(self):
        self.var_email_id.set("")
        self.var_dog_id.set("")
        self.var_adoption.set("")

    def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="yashmysql21", database="dognation")
        my_cursor = conn.cursor()

        p = str(self.search_var.get())
        if p == "email_id":
            select_stmt = "SELECT dog.dog_id,users.email_id,dog.breed_name,dog.gender,dog.weight,health.neuter_status,health.dna_test,health.special_needs,health.age,dog.adoption,users.liking,dog.liking,users.user_id from dog INNER JOIN health ON dog.dog_id=health.dog_id INNER JOIN users ON dog.liking=users.liking WHERE users.email_id = %(email_id)s AND dog.adoption = 0 AND dog.breed_name = users.breed_want"
            my_cursor.execute(select_stmt, { 'email_id': str(self.txt_search.get()) })
            #my_cursor.execute("SELECT dog.dog_id,health.neuter_status,health.age,dog.breed_name,dog.gender,dog.weight,health.special_needs,health.dna_test,dog.adoption,users.liking,dog.liking from dog INNER JOIN health ON dog.dog_id=health.dog_id INNER JOIN users ON dog.liking=users.liking WHERE users.email_id ="
            #+str(self.txt_search.get())+ " `and` dog.adoption = 0 ")
        #+ str(self.search_var.get()) + "=" 
        else:
            select1_stmt = "SELECT dog.dog_id,users.email_id,dog.breed_name,dog.gender,dog.weight,health.neuter_status,health.dna_test,health.special_needs,health.age,dog.adoption,users.liking,dog.liking,users.user_id from dog INNER JOIN health ON dog.dog_id=health.dog_id INNER JOIN users ON dog.liking=users.liking WHERE users.name = %(name)s AND dog.adoption = 0 AND dog.breed_name = users.breed_want"
            my_cursor.execute(select1_stmt, { 'name': str(self.txt_search.get()) })
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.adoptdog.delete(*self.adoptdog.get_children())
            for i in rows:
                self.adoptdog.insert("", END, values=i)
            conn.commit()
        conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = adopt_dog(root)
    root.mainloop()





