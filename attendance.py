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
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1284x760")  # Match to image size
        self.root.title("Attendance Data")

# ================ Variables =============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        self.var_gender = StringVar()




    # Background Image
        img2 = Image.open("photos/bg.jpg")
        img2 = img2.resize((1284, 690), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        bg_label = Label(self.root, image=self.photoimg2)
        bg_label.place(x=0, y=70, width=1284, height=690)

    # Image left
        img_left = Image.open("photos/image1.png")
        img_left = img_left.resize((1280, 170), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        left_label = Label(self.root, image=self.photoimg_left)
        left_label.place(x=0, y=0, width=1280, height=170)
    
    # Title
        title_lbl = Label(self.root, text="Attendance Management System", font=("time new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=150, width=1330, height=50)
    
        main_frame = Frame(bg_label,bd=2, bg="white")
        main_frame.place(x=10,y=136,width=1254, height=470)

    #Left Side Label
        left_frame = LabelFrame(main_frame,bd = 2, relief = RIDGE, text="Student Details", font=("times new roman",12,"bold"), bg="white")
        left_frame.place(x = 10 , y = 0 , width = 650, height=460)

        img_left = Image.open("photos/header.jpg")
        img_left = img_left.resize((1284, 70), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        left_label = Label(left_frame, image=self.photoimg_left)
        left_label.place(x=0, y=-3, width=1284, height=70)
    
    #Right Side Label
        right_frame = LabelFrame(main_frame,bd = 2, relief =     RIDGE, text="Open CV Frame", font=("times new roman",12,"bold"), bg="white")
        right_frame.place(x = 620 , y = 0 , width = 630, height=460)

        img_right = Image.open("photos/header.jpg")
        img_right = img_right.resize((1284, 70), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        right_label = Label(right_frame, image=self.photoimg_right)
        right_label.place(x=0, y=0, width=1284, height=64)


        left_inside_frame = Frame(left_frame,bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=3,y=70,width=590, height=363)
    
       # Right side frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=2, y=67, width=621, height=385)
        # For scroll Bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.AttendanceReport = ttk.Treeview(table_frame,columns=("ID","Roll No","Name","Department","Time","Date","Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReport.xview)
        scroll_y.config(command=self.AttendanceReport.yview)

        self.AttendanceReport.heading("ID",text="Attendance ID")
        self.AttendanceReport.heading("Roll No",text="Roll No")
        self.AttendanceReport.heading("Name",text="Name")
        self.AttendanceReport.heading("Department",text="Department")
        self.AttendanceReport.heading("Time",text="Time")
        self.AttendanceReport.heading("Date",text="Date")
        self.AttendanceReport.heading("Status",text="Status")
        self.AttendanceReport["show"] = "headings"

        self.AttendanceReport.column("ID",width=100)
        self.AttendanceReport.column("Roll No",width=100)
        self.AttendanceReport.column("Name",width=100)
        self.AttendanceReport.column("Department",width=100)
        self.AttendanceReport.column("Time",width=100)
        self.AttendanceReport.column("Date",width=100)
        self.AttendanceReport.column("Status",width=100)
        
        self.AttendanceReport.pack(fill=BOTH,expand=1)
        self.AttendanceReport.bind("<ButtonRelease-1>",self.get_cursor)

    
        
       
        # Label and Entry
        attendance_label = Label(right_frame, image=self.photoimg_right)
        attendance_label.place(x=0, y=0, width=1284, height=64)
        
        # Row 0
        attendance_id_label = Label(left_inside_frame, text="Attendance ID", font=("times new roman", 12, "bold"))
        attendance_id_label.grid(row=0, column=0, padx=10, pady=8, sticky="w")
        student_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_id, font=("times new roman", 12, "bold"))
        student_entry.grid(row=0, column=1, padx=10)
        
        rollNumber_label = Label(left_inside_frame, text="Roll No.", font=("times new roman", 12, "bold"))
        rollNumber_label.grid(row=0, column=2, padx=10, pady=8, sticky="w")
        rollNumber_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_roll, font=("times new roman", 12, "bold"))
        rollNumber_entry.grid(row=0, column=3, padx=10)
        
        # Row 1
        name_id_label = Label(left_inside_frame, text="Name", font=("times new roman", 12, "bold"))
        name_id_label.grid(row=1, column=0, padx=10, pady=8, sticky="w")
        name_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_name, font=("times new roman", 12, "bold"))
        name_entry.grid(row=1, column=1, padx=10)
        
        department_label = Label(left_inside_frame, text="Department", font=("times new roman", 12, "bold"))
        department_label.grid(row=1, column=2, padx=10, pady=8, sticky="w")
        department_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_dep,font=("times new roman", 12, "bold"))
        department_entry.grid(row=1, column=3, padx=10)
        
        # Row 2
        time_label = Label(left_inside_frame, text="Time", font=("times new roman", 12, "bold"))
        time_label.grid(row=2, column=0, padx=10, pady=8, sticky="w")
        time_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_time, font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=10)
        
        date_label = Label(left_inside_frame, text="Date", font=("times new roman", 12, "bold"))
        date_label.grid(row=2, column=2, padx=10, pady=8, sticky="w")
        date_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_date, font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=3, padx=10)
    
        # Row 3
        gender = Label(left_inside_frame, text="Gender", font=("times new roman", 12, "bold"))
        gender.grid(row=3, column=0, padx=10, pady=8, sticky="w")
       # gender_entry = ttk.Entry(class_student_frame,textvariable=self.var_gender, width=20, font=("times new roman", 12, "bold"))
       # gender_entry.grid(row=2, column=1, padx=10)
        
        gender_combo = ttk.Combobox(left_inside_frame, font=("times new roman",12,"bold"), textvariable=self.var_gender,state="readonly",width=18)
        gender_combo["values"] = ("Status","Present","Absent")
        gender_combo.current(0)
        gender_combo.grid(row=3, column=1, padx=15, pady=5, sticky="w")
    
            # Button Frame
    
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=2, y=200, width=590, height=161)
        
        # Row 0: Standard CRUD buttons
        import_btn = Button(btn_frame,command=self.import_csv,text="Import CSV", width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0)
        
        export_btn = Button(btn_frame,command=self.export_csv, text="Export CSV", width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1)
        
        update_btn = Button(btn_frame, text="Update", width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2)
        
        reset_btn = Button(btn_frame,text="Reset", width=14,command=self.reset_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)
        
    def fetch_data(self,rows):
        self.AttendanceReport.delete(*self.AttendanceReport.get_children())
        for i in rows:
            self.AttendanceReport.insert("",END,values=i)
    
    def import_csv(self):
       global mydata 
       mydata.clear()
       fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")))
       with open(fln) as myfile:
           csvreader = csv.reader(myfile,delimiter=",")
           for i in csvreader:
               mydata.append(i)
           self.fetch_data(mydata) 
    # Export CSV
    def export_csv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data","No Data Found To Export")
                return False
            fln= filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")))
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to" + os.path.basename(fln)+"successfully")
        except Exception as es: messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)
     
    # Cursor 
    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReport.focus()
        content = self.AttendanceReport.item(cursor_row)
        rows = content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_gender.set(rows[6])
    
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_gender.set("Status")





  



if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)

    root.mainloop()
