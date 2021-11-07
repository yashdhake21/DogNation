from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class about_details:
    def __init__(self, root):
        self.root = root
        self.root.title("DOGNATION")
        # Put frame geometry starting from 0, 0
        self.root.geometry("600x400+0+0")
        text1 = "The main aim is to design a system that would easily help an "
        text2 = "adoptee find a pet that matches their preferences. This will "
        text3 = "be done by considering various factors according to the users  "
        text4 = "needs. Incase an owner loses their dog, we aim to help them "
        text5 = "find their dog by using our centralised rescued dog database."
        lbl1 = Label(self.root, text="About", font=("arial", 18, "bold"), bg="black",
                     fg="orange", bd=4, relief=RIDGE)
        lbl1.place(x=0, y=0, width=600, height=50)

        lableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="", padx=2, font=("arial", 12, "bold"))
        lableframe.place(x=5, y=55, width=600, height=400)

        lbl2 = Label(lableframe, text="Developers: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl2.grid(row=0, column=0, sticky=W)

        lbl3 = Label(lableframe, text="Yash Dhake ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl3.grid(row=0, column=1, sticky=W)

        lbl4 = Label(lableframe, text="Varun Taneja", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl4.grid(row=1, column=1, sticky=W)

        lbl5 = Label(lableframe, text=text1, font=("arial", 12, "bold"), padx=2, pady=6)
        lbl5.grid(row=2, column=1, sticky=W)

        lbl6 = Label(lableframe, text=text2, font=("arial", 12, "bold"), padx=2, pady=6)
        lbl6.grid(row=3, column=1, sticky=W)

        lbl7 = Label(lableframe, text=text3, font=("arial", 12, "bold"), padx=2, pady=6)
        lbl7.grid(row=4, column=1, sticky=W)

        lbl8 = Label(lableframe, text=text4, font=("arial", 12, "bold"), padx=2, pady=6)
        lbl8.grid(row=5, column=1, sticky=W)

        lbl9 = Label(lableframe, text=text5, font=("arial", 12, "bold"), padx=2, pady=6)
        lbl9.grid(row=6, column=1, sticky=W)

        lbl10 = Label(lableframe, text="About: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl10.grid(row=2, column=0, sticky=W)

if __name__ == "__main__":
    root = Tk()
    obj = about_details(root)
    root.mainloop()

