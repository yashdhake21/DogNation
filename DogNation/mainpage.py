from tkinter import *
from PIL import Image, ImageTk
from user import user_details
from dog import dog_details
from lostdog import lostdog
from adoptdog import adopt_dog
from location import location_details
from About import about_details
import sys
import tkinter.font

class DogNation:
    def __init__(self, root):
        self.root = root
        self.root.title("DOGNATION")
        # Put frame geometry starting from 0, 0
        self.root.geometry("1550x800+0+0")

        # Header Images
        img1 = Image.open("40.jpg")
        img1 = img1.resize((220, 140), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl1 = Label(self.root, image=self.photoimg1, bd=1, relief=RIDGE)
        lbl1.place(x=235, y=0, width=220, height=140)

        img1b = Image.open("41.jpg")
        img1b = img1b.resize((220, 140), Image.ANTIALIAS)
        self.photoimg1b = ImageTk.PhotoImage(img1b)
        lbl1b = Label(self.root, image=self.photoimg1b, bd=1, relief=RIDGE)
        lbl1b.place(x=455, y=0, width=220, height=140)

        img1c = Image.open("44.jpeg")
        img1c = img1c.resize((220, 140), Image.ANTIALIAS)
        self.photoimg1c = ImageTk.PhotoImage(img1c)
        lbl1c = Label(self.root, image=self.photoimg1c, bd=1, relief=RIDGE)
        lbl1c.place(x=675, y=0, width=220, height=140)

        img1d = Image.open("44.jpg")
        img1d = img1d.resize((220, 140), Image.ANTIALIAS)
        self.photoimg1d = ImageTk.PhotoImage(img1d)
        lbl1d = Label(self.root, image=self.photoimg1d, bd=1, relief=RIDGE)
        lbl1d.place(x=895, y=0, width=220, height=140)

        img1e = Image.open("45.jpg")
        img1e = img1e.resize((220, 140), Image.ANTIALIAS)
        self.photoimg1e = ImageTk.PhotoImage(img1e)
        lbl1e = Label(self.root, image=self.photoimg1e, bd=1, relief=RIDGE)
        lbl1e.place(x=1115, y=0, width=220, height=140)

        img1f = Image.open("48.jpg")
        img1f = img1f.resize((220, 140), Image.ANTIALIAS)
        self.photoimg1f = ImageTk.PhotoImage(img1f)
        lbl1f = Label(self.root, image=self.photoimg1f, bd=1, relief=RIDGE)
        lbl1f.place(x=1335, y=0, width=220, height=140)

        # Logo
        img2 = Image.open("47.jpg")
        img2 = img2.resize((235, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl2 = Label(self.root,image=self.photoimg2, bd=1, relief=RIDGE)
        lbl2.place(x=0, y=0, width=235, height=140)

        # Main Frame
        main_frame = Frame(self.root, bd=1, relief=RIDGE)
        main_frame.place(x=0, y=140, width=1555, height=670)

        # Menu
        lbl4 = Label(main_frame, text="MENU", font=("Arial", 18, "bold"), bg="black",
                     fg="white", bd=8, relief=RIDGE)
        lbl4.place(x=0, y=280, width=235, height= 65)

        # Menu Frame
        menu_frame = Frame(main_frame, background="black",bd=2, relief=RIDGE)
        menu_frame.place(x=0, y=345, width=235, height=335)

        user_btn = Button(menu_frame, text="USER", command=self.user_details, width=15, font=("Arial", 14, "bold"), bg="black",
                     fg="white", bd=5, cursor="hand1")
        user_btn.grid(row=0, column=0, pady=0)

        dog_btn = Button(menu_frame, text="DOG DETAILS",command=self.dog_details, width=15, font=("Arial", 14, "bold"), bg="black",
                              fg="white", bd=5, cursor="hand1")
        dog_btn.grid(row=1, column=0, pady=0)

        lostdog_btn = Button(menu_frame, text="FIND LOST DOGS", command=self.lost_dog, width=15, font=("Arial", 14, "bold"), bg="black",
                              fg="white", bd=5, cursor="hand1")
        lostdog_btn.grid(row=2, column=0, pady=0)

        adoptdog_btn = Button(menu_frame, text="ADOPT A DOG",command=self.adopt_dog, width=15, font=("Arial", 14, "bold"), bg="black",
                              fg="white", bd=5, cursor="hand1")
        adoptdog_btn.grid(row=3, column=0, pady=0)

        location_btn = Button(menu_frame, text= "LOCATION",command=self.Location,width=15, font=("Arial", 14, "bold"), bg="black",
                              fg="white", bd=5, cursor="hand1")
        location_btn.grid(row=4, column=0, pady=0)

        about_btn = Button(menu_frame, text= "ABOUT",width=15,command=self.About, font=("Arial", 14, "bold"), bg="black",
                              fg="white", bd=5, cursor="hand1")
        about_btn.grid(row=5, column=0, pady=0)

        logout_btn = Button(menu_frame, text="LOGOUT",command=self.Logout, width=15, font=("Arial", 14, "bold"), bg="black",
                              fg="white", bd=5, cursor="hand1")
        logout_btn.grid(row=6, column=0, pady=0, padx=22)

        # Centre Image
        img3 = Image.open("3.png")
        img3 = img3.resize((1315, 665), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl5 = Label(main_frame, image=self.photoimg3, bd=2, relief=RIDGE)
        lbl5.place(x=235, y=0, width=1315, height=665)

        # Side Images
        img4 = Image.open("49.jpg")
        img4 = img4.resize((234, 140), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lbl6 = Label(main_frame, image=self.photoimg4, bd=1, relief=RIDGE)
        lbl6.place(x=0, y=0, width=234, height=140)

        img5 = Image.open("50.jpeg")
        img5 = img5.resize((234, 140), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lbl7 = Label(main_frame, image=self.photoimg5, bd=1, relief=RIDGE)
        lbl7.place(x=0, y=140, width=234, height=140)

    def user_details(self):
        self.new_window = Toplevel(self.root)
        self.app = user_details(self.new_window)
    
    def dog_details(self):
        self.new_window = Toplevel(self.root)
        self.app = dog_details(self.new_window)

    def lost_dog(self):
        self.new_window = Toplevel(self.root)
        self.app = lostdog(self.new_window)

    def adopt_dog(self):
        self.new_window = Toplevel(self.root)
        self.app = adopt_dog(self.new_window)

    def Location(self):
        self.new_window = Toplevel(self.root)
        self.app = location_details(self.new_window)

    def About(self):
        self.new_window = Toplevel(self.root)
        self.app = about_details(self.new_window)
    
    def Logout(self):
        sys.exit(0)  


if __name__ == "__main__":
    root = Tk()
    obj = DogNation(root)
    root.mainloop()

