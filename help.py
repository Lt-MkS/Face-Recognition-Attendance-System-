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
class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1284x760")  # Match to image size
        self.root.title("Attendance Data")
        title_lbl = Label(self.root, text="Help Desk", font=("time new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1330, height=45)
        # Top Image
        img_top = Image.open("photos/help_image.png")
        img_top = img_top.resize((1284, 640), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        top_label = Label(self.root, image=self.photoimg_top)
        top_label.place(x=0, y=50, width=1284, height=640)

        email_label = Label(self.root,text="Email : mayanks.cs.22@nitj.ac.in", font=("times new roman",20,"bold"),bg="white",fg="black")
        email_label.place(x=430,y=220)

      








if __name__ == "__main__":
    root = Tk()
    obj = Help(root)

    root.mainloop()
