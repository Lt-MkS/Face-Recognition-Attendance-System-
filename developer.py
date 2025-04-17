from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
import numpy as np
from time import strftime
from datetime import datetime
from tkinter import filedialog
mydata = []
class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1284x760")  # Match to image size
        self.root.title("Attendance Data")
        title_lbl = Label(self.root, text="Developer", font=("time new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1330, height=45)
        # Top Image
        img_top = Image.open("photos/developers_image.png")
        img_top = img_top.resize((1284, 640), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        top_label = Label(self.root, image=self.photoimg_top)
        top_label.place(x=0, y=50, width=1284, height=640)

        main_frame = Frame(top_label,bd=2, bg="white")
        main_frame.place(x=750,y=5,width=515, height=625)

        img_top1 = Image.open("photos/mayank_pic.png")
        img_top1 = img_top1.resize((200, 240), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        top_label1 = Label(main_frame, image=self.photoimg_top1)
        top_label1.place(x=310, y=0, width=200, height=240)

        # Developer Info 
        dev_label = Label(main_frame, text="Mayank Sehgal", font=("times new roman",12,"bold"))
        dev_label.place(x=0,y=5,width= 150,height=30)

        dev1_label = Label(main_frame, text="CSE 3rd year NIT Jalandhar", font=("times new roman",12,"bold"))
        dev1_label.place(x=0,y=35,width= 236,height=30)

        dev2_label = Label(main_frame, text="ML Enginner", font=("times new roman",12,"bold"))
        dev2_label.place(x=0,y=65,width= 136,height=30)
    
    


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)

    root.mainloop()
