#Adopt a dog
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class lostdog:
    def __init__(self, root):
        self.root = root
        self.root.title("DogNation")
        # Put frame geometry starting from 0, 0
        self.root.geometry("1295x550+0+0")
        # Variables
        self.var_breed_name = StringVar()
        self.var_dog_id = StringVar()
        self.var_gender = StringVar()
        self.var_weight = StringVar()
        self.var_location_id = StringVar()
        self.var_dog_size = StringVar()
        self.var_tag_name = StringVar() 
        self.var_age = StringVar() 

        # Title
        lbl1 = Label(self.root, text="FIND LOST DOG", font=("Arial", 18, "bold"), bg="black",
                     fg="orange", bd=4, relief=RIDGE)
        lbl1.place(x=0, y=0, width=1295, height=50)

        # Label Frame
        lableframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="LOST DOG DETAILS", padx=2,
                                    font=("Arial", 12, "bold"), bg="black", fg="white")
        lableframeleft.place(x=5, y=50, width=425, height=530)

        # Lost Dog Details
        # dog_id
        lbl_lost_dog_id = Label(lableframeleft, text="Dog ID : ", font=("Arial", 12, "bold"), padx=2,
                            pady=6, bg="black", fg="white")
        lbl_lost_dog_id.grid(row=0, column=0, sticky=W)
        entry_lost_dog_id = ttk.Entry(lableframeleft, textvariable=self.var_dog_id, width=25,
                                  font=("Arial", 11, "bold"), state="readonly")
        entry_lost_dog_id.grid(row=0, column=1, sticky=W)

        # breed_name
        lbl_lost_breed_name = Label(lableframeleft, text="Breed Name : ", font=("Arial", 12, "bold"), padx=2,
                            pady=6, bg="black", fg="white")
        lbl_lost_breed_name.grid(row=1, column=0, sticky=W)
        entry_lost_breed_name = ttk.Entry(lableframeleft, textvariable=self.var_breed_name, width=25,
                                  font=("Arial", 11, "bold"))
        entry_lost_breed_name.grid(row=1, column=1)

        # # Buttons
        # btn_frame = Frame(lableframeleft, bg="black",relief=RIDGE)
        # btn_frame.place(x=0, y=350, width=412, height=40)

        # btnAdd = Button(btn_frame, text="ADD", command=self.add_data, font=("Arial", 12, "bold"), bg="orange", fg="white",
        #                  width=10, padx=1)
        # btnAdd.grid(row=0, column=0)

        # btnUpdate = Button(btn_frame, text="UPDATE", command=self.update, font=("Arial", 12, "bold"),
        #                    bg="orange", fg="white", width=10, padx=1)
        # btnUpdate.grid(row=0, column=1)

        # btnDelete = Button(btn_frame, text="DELETE", command=self.mDelete, font=("Arial", 12, "bold"),
        #                     bg="orange", fg="white", width=10, padx=1)
        # btnDelete.grid(row=0, column=2)

        # btnReset = Button(btn_frame, text="RESET", command=self.reset, font=("Arial", 12, "bold"), bg="orange", fg="white", width=10, padx=1)
        # btnReset.grid(row=0, column=3)

        # Table Frame
        TableFrame = LabelFrame(self.root, bd=2, relief=RIDGE, text="VIEW DETAILS AND SEARCH SYSTEM", padx=2,
                                font=("Arial", 12, "bold"))
        TableFrame.place(x=435, y= 10, width=860, height=560)

        lbl_searchby = Label(TableFrame, text="Search By : ", font=("Arial", 12, "bold"), bg="orange",
                             fg="white")
        lbl_searchby.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(TableFrame,textvariable=self.search_var,font=("Arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("breed_name")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        entry_lostdog_search = ttk.Entry(TableFrame,textvariable=self.txt_search,width=24, font=("Arial", 13, "bold"))
        entry_lostdog_search.grid(row=0, column=2, padx=2)

        self.search_var1 = StringVar()
        combo_search = ttk.Combobox(TableFrame,textvariable=self.search_var1,font=("Arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("Age")
        combo_search.current(0)
        combo_search.grid(row=1, column=1, padx=2, pady=2)

        self.search_age = StringVar()
        entry_lostdog_search = ttk.Entry(TableFrame,textvariable=self.search_age,width=24, font=("Arial", 13, "bold"))
        entry_lostdog_search.grid(row=1, column=2, padx=2)

        self.search_var2 = StringVar()
        combo_search = ttk.Combobox(TableFrame,textvariable=self.search_var2,font=("Arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("dog_size")
        combo_search.current(0)
        combo_search.grid(row=2, column=1, padx=2, pady=3)

        self.search_dog_size = StringVar()
        entry_lostdog_search = ttk.Entry(TableFrame,textvariable=self.search_dog_size,width=24, font=("Arial", 13, "bold"))
        entry_lostdog_search.grid(row=2, column=2, padx=2)

        btnSearch = Button(TableFrame, text="SEARCH", command=self.search, font=("Arial", 12, "bold"),
                           bg="black", fg="orange", width=10, padx=1, height=1)
        btnSearch.grid(row=0, column=3, padx=2)

        btnShowAll = Button(TableFrame, text="SHOW ALL", command=self.fetch_data, font=("Arial", 12, "bold"),
                            bg="black", fg="orange", width=10, padx=1, height=1)
        btnShowAll.grid(row=0, column=4, padx=2)

        # Show Data Table
        DetailsFrame = Frame(TableFrame, bd=2, relief=RIDGE)
        DetailsFrame.place(x=0, y=120, width=830, height=380)

        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)

        self.lost_dog = ttk.Treeview(DetailsFrame, column=("dog_id", "breed_name", "age", "location_id", "gender", "weight", "dog_size" , "tag_name"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.lost_dog.xview)
        scroll_y.config(command=self.lost_dog.yview)

        self.lost_dog.heading("dog_id", text="Dog ID")
        self.lost_dog.heading("breed_name", text="Breed Name")
        self.lost_dog.heading("age", text="Age")
        self.lost_dog.heading("location_id", text="Location ID")
        self.lost_dog.heading("gender", text="Gender")
        self.lost_dog.heading("weight", text="Weight")
        self.lost_dog.heading("dog_size", text="Dog Size")
        self.lost_dog.heading("tag_name", text="Name on DogTag")

        self.lost_dog["show"] = "headings" 
        self.lost_dog.column("dog_id", width=100)
        self.lost_dog.column("breed_name", width=100)
        self.lost_dog.column("age", width=100)
        self.lost_dog.column("location_id", width=100)
        self.lost_dog.column("gender", width=100)
        self.lost_dog.column("weight", width=100)
        self.lost_dog.column("dog_size", width=100)
        self.lost_dog.column("tag_name", width=100)
               

        self.lost_dog.pack(fill=BOTH, expand=1)
        self.lost_dog.bind("<ButtonRelease-1>",self.get_cursor)
        #self.fetch_data()

    def fetch_data(self):
            conn = mysql.connector.connect(host="localhost", user="root", password="yashmysql21", database="dognation")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT lost.dog_id, lost.breed_name , lost.age , lost.location_id , lost.gender , looks.weight , looks.dog_size , dogtag.tag_name FROM lost INNER JOIN dogtag ON lost.dog_id=dogtag.dog_id INNER JOIN looks ON lost.dog_id=looks.dog_id;")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.lost_dog.delete(*self.lost_dog.get_children())
                for i in rows:
                    self.lost_dog.insert("", END, values=i)
                conn.commit()
            conn.close()

    def get_cursor(self, events=""):
        cursor_row = self.lost_dog.focus()
        content = self.lost_dog.item(cursor_row)
        row = content["values"]

        self.var_dog_id.set(row[0]),
        self.var_breed_name.set(row[1]),
        self.var_age.set(row[2]),
        self.var_location_id.set(row[3]),
        self.var_gender.set(row[4]),
        self.var_weight.set(row[5])
        self.var_dog_size.set(row[6])
        self.var_tag_name.set(row[7])

    def reset(self):
        self.var_dog_id.set(""),
        self.var_breed_name.set(""),
        
    def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="yashmysql21", database="dognation")
        my_cursor = conn.cursor()

        p = str(self.search_var.get())
        #q = str(self.search_var1.get())
        #r = str(self.search_var2.get())
        if p == "breed_name":
            #select_stmt = "SELECT lost.dog_id,lost.breed_name,lost.age,lost.location_id,lost.gender,looks.weight,looks.dog_size,dogtag.tag_name FROM lost INNER JOIN dogtag ON lost.dog_id=dogtag.dog_id INNER JOIN looks ON lost.dog_id=looks.dog_id WHERE lost.breed_name = %(breed_name)s or lost.age < %(age)s or looks.dog_size = %(dog_size)s ;"
            select_stmt = "SELECT lost.dog_id,lost.breed_name,lost.age,lost.location_id,lost.gender,looks.weight,looks.dog_size,dogtag.tag_name FROM lost INNER JOIN dogtag ON lost.dog_id=dogtag.dog_id INNER JOIN looks ON lost.dog_id=looks.dog_id WHERE lost.breed_name = %(breed_name)s and lost.age < %(age)s and looks.dog_size = %(dog_size)s"
            #my_cursor.execute(select_stmt, { 'breed_name': str(self.txt_search.get()),'age': str(self.search_age.get()),'weight': str(self.search_dog_size())})
            my_cursor.execute(select_stmt, { 'breed_name': str(self.txt_search.get()),'age': str(self.search_age.get()),'dog_size': str(self.search_dog_size.get())})

        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.lost_dog.delete(*self.lost_dog.get_children())
            for i in rows:
                self.lost_dog.insert("", END, values=i)
            conn.commit()
        conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = lostdog(root)
    root.mainloop()





