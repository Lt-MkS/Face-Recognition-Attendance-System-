from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
class student_details:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1284x760")  # Match to image size
        self.root.title("Student Details")
    

# =============== Variables =================
        # ==========variables==========
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()




        # Header Image
        img1 = Image.open("photos/header.jpg")
        img1 = img1.resize((1284, 70), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        header_label = Label(self.root, image=self.photoimg1)
        header_label.place(x=0, y=0, width=1284, height=70)
        
        # Background Image
        img2 = Image.open("photos/bg.jpg")
        img2 = img2.resize((1284, 690), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        bg_label = Label(self.root, image=self.photoimg2)
        bg_label.place(x=0, y=70, width=1284, height=690)
        
        # Title
        title_lbl = Label(bg_label, text="Student Management System", font=("time new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1330, height=50)

        main_frame = Frame(bg_label,bd=2, bg="white")
        main_frame.place(x=5,y=5,width=1260, height=605)
        
        #Left Side Label
        left_frame = LabelFrame(main_frame,bd = 2, relief = RIDGE, text="Student Details", font=("times new roman",12,"bold"), bg="white")
        left_frame.place(x = 10 , y = 0 , width = 600, height=590)

        img_left = Image.open("photos/header.jpg")
        img_left = img_left.resize((1284, 70), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        left_label = Label(left_frame, image=self.photoimg1)
        left_label.place(x=0, y=-3, width=1284, height=70)

    
        # Class Student Information 
        class_student_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"), bg="white")
        class_student_frame.place(x=0, y=185, width=598, height=380)  # Slightly increased height
        
        current_course_frame = LabelFrame(left_frame,bd = 2, relief = RIDGE, text="Current Course Information", font=("times new roman",12,"bold"), bg="white")
        current_course_frame.place(x = 0 , y = 65, width = 598, height=115)


        # Department 
        dept_label = Label(current_course_frame, text="Department", font=("times new roman",12,"bold"))
        dept_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman",12,"bold"), state="readonly")
        dep_combo["values"] = ("Select Department","Computer Science","Civil","ECE","ICE")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman",12,"bold"))
        course_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        
        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman",12,"bold"), state="readonly")
        course_combo["values"] = ("Select Course","Machine Learning","DAA","DSA","Mathematics I")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=10, pady=5, sticky="w")
        
        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman",12,"bold"))
        year_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman",12,"bold"), state="readonly")
        year_combo["values"] = ("Select Year","I","II","III","IV")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman",12,"bold"))
        semester_label.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        
        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman",12,"bold"), state="readonly")
        semester_combo["values"] = ("Select Semester","I","II","III","IV","V","VI","VII","VIII")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=10, pady=5, sticky="w")








        # Row 0
        student_id_label = Label(class_student_frame, text="Student ID", font=("times new roman", 12, "bold"))
        student_id_label.grid(row=0, column=0, padx=10, pady=8, sticky="w")
        student_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id,width=20, font=("times new roman", 12, "bold"))
        student_entry.grid(row=0, column=1, padx=10)
        
        student_name_label = Label(class_student_frame, text="Student Name", font=("times new roman", 12, "bold"))
        student_name_label.grid(row=0, column=2, padx=10, pady=8, sticky="w")
        student_name_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
        student_name_entry.grid(row=0, column=3, padx=10)
        
        # Row 1
        class_division = Label(class_student_frame, text="Class Division", font=("times new roman", 12, "bold"))
        class_division.grid(row=1, column=0, padx=10, pady=8, sticky="w")
       # class_entry = ttk.Entry(class_student_frame, textvariable=self.var_div,width=20, font=("times new roman", 12, "bold"))
       # class_entry.grid(row=1, column=1, padx=10)

        division_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=("times new roman",12,"bold"), state="readonly",width=18)
        division_combo["values"] = ("Select Div","A","B","C")
        division_combo.current(0)
        division_combo.grid(row=1, column=1, padx=15, pady=10, sticky="w")
        
        roll_no_label = Label(class_student_frame, text="Roll No.", font=("times new roman", 12, "bold"))
        roll_no_label.grid(row=1, column=2, padx=10, pady=8, sticky="w")
        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10)
        
        # Row 2
        gender = Label(class_student_frame, text="Gender", font=("times new roman", 12, "bold"))
        gender.grid(row=2, column=0, padx=10, pady=8, sticky="w")
      # gender_entry = ttk.Entry(class_student_frame,textvariable=self.var_gender, width=20, font=("times new roman", 12, "bold"))
      # gender_entry.grid(row=2, column=1, padx=10)
        
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman",12,"bold"), state="readonly",width=18)
        gender_combo["values"] = ("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=15, pady=5, sticky="w")

       
        
        DOB = Label(class_student_frame, text="DOB", font=("times new roman", 12, "bold"))
        DOB.grid(row=2, column=2, padx=10, pady=8, sticky="w")
        DOB_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob, width=20, font=("times new roman", 12, "bold"))
        DOB_entry.grid(row=2, column=3, padx=10)
        
        # Row 3
        email = Label(class_student_frame, text="Email", font=("times new roman", 12, "bold"))
        email.grid(row=3, column=0, padx=10, pady=8, sticky="w")
        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10)
        
        phone_no = Label(class_student_frame, text="Phone No.", font=("times new roman", 12, "bold"))
        phone_no.grid(row=3, column=2, padx=10, pady=8, sticky="w")
        phone_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        phone_no_entry.grid(row=3, column=3, padx=10)
        
        # Row 4
        address = Label(class_student_frame, text="Address", font=("times new roman", 12, "bold"))
        address.grid(row=4, column=0, padx=10, pady=8, sticky="w")
        address_entry = ttk.Entry(class_student_frame,textvariable = self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10)
        
        teacher = Label(class_student_frame, text="Teacher Name", font=("times new roman", 12, "bold"))
        teacher.grid(row=4, column=2, padx=10, pady=8, sticky="w")
        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10)

        
        # Radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row = 5,column=0)

        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row = 5,column=1)

        # Buttons Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=2, y=240, width=590, height=115)
        
        # Row 0: Standard CRUD buttons
        save_btn = Button(btn_frame, command=self.add_data,text="Save", width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)
        
        reset_btn = Button(btn_frame, command=self.reset_data,text="Reset", width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=1)
        
        update_btn = Button(btn_frame, command=self.update_data,text="Update", width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2)
        
        delete_btn = Button(btn_frame,command=self.delete_data, text="Delete", width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=3)
        
        # Row 1: Photo buttons
        take_photo_btn = Button(btn_frame,command=self.generate_dataset, text="Take Photo Sample", width=30, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=1, column=0, columnspan=2, pady = 5)
        
        update_photo_btn = Button(btn_frame, text="Update Photo Sample", width=29, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=1, column=2, columnspan=2, pady = 5)







    #Right Side Label
        right_frame = LabelFrame(main_frame,bd = 2, relief = RIDGE, text="Open CV Frame", font=("times new roman",12,"bold"), bg="white")
        right_frame.place(x = 620 , y = 0 , width = 630, height=590)
        
        img_right = Image.open("photos/header.jpg")
        img_right = img_right.resize((1284, 70), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        right_label = Label(right_frame, image=self.photoimg_right)
        right_label.place(x=0, y=0, width=1284, height=64)


      # ---------------------------   Search System  ------------------------

       # Class Student Information 
        search_student_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, text="Search Student Frame", font=("times new roman", 12, "bold"), bg="white")
        search_student_frame.place(x=0, y=65, width=625, height=380)  # Slightly increased height
        
        search_frame = Label(search_student_frame, text="Search By : ", font=("times new roman", 12, "bold"), bg="red")
        search_frame.grid(row=2, column=0,sticky="w")
       
        search_combo = ttk.Combobox(search_student_frame, font=("times new roman",12,"bold"), state="readonly")
        search_combo["values"] = ("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=2, column=1, padx=5, pady=5, sticky="w")
       
        phone_entry = ttk.Entry(search_student_frame, width=15, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=2, column=2,padx=2)

        search_btn = Button(search_student_frame, text="Search", width=9, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        search_btn.grid(row=2, column=3,padx=3)
        
        show_all_btn = Button(search_student_frame, text="Show All", width=9, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        show_all_btn.grid(row=2, column=4)

# Table Frame 
        
        table_frame = Frame(right_frame,bd=2,bg="red",relief=RIDGE)
        table_frame.place(x = 0, y =120,width=622,height=446)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=("a","b","c","d","e","f","g","h","i","j","k","l","m"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)        
        
        self.student_table.heading("a", text="Department")
        self.student_table.heading("b", text="Course")
        self.student_table.heading("c", text="Year")
        self.student_table.heading("d", text="Semester")
        self.student_table.heading("e", text="StudentId")
        self.student_table.heading("f", text="Name")
        self.student_table.heading("g", text="Division")
        self.student_table.heading("h", text="DOB")
        self.student_table.heading("i", text="Email")
        self.student_table.heading("j", text="Phone")
        self.student_table.heading("k", text="Address")
        self.student_table.heading("l", text="Teacher")
        self.student_table.heading("m", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("a", width=100)   
        self.student_table.column("b", width=100)   
        self.student_table.column("c", width=100)   
        self.student_table.column("d", width=100)   
        self.student_table.column("e", width=100)   
        self.student_table.column("f", width=100)   
        self.student_table.column("g", width=100)   
        self.student_table.column("h", width=100)   
        self.student_table.column("i", width=100)   
        self.student_table.column("j", width=100)   
        self.student_table.column("k", width=100)   
        self.student_table.column("l", width=100)   
        self.student_table.column("m", width=100)   
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

## ------------------------Function Defination-------------------------
    def add_data(self):  
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error","All Fields are required")
        else:
            try:

                conn = mysql.connector.connect(host= "localhost",username = "root", password ="Assehgal1@",database= "face_recognization_system")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                         self.var_dep.get(),
                         self.var_course.get(),
                         self.var_year.get(),
                         self.var_semester.get(),
                         self.var_std_id.get(),  
                         self.var_std_name.get(),
                         self.var_div.get(),
                         self.var_dob.get(),
                         self.var_email.get(),
                         self.var_phone.get(),
            
                         self.var_address.get(),
                         self.var_teacher.get(),

                         self.var_radio1.get(),
                         
                         self.var_roll.get(),
                         self.var_gender.get()

                                     ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details Added Successfully",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
    # =============================== Fetch Data =============================
    def fetch_data(self):
        conn = mysql.connector.connect(host= "localhost",username = "root", password ="Assehgal1@",database= "face_recognization_system")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    
    # ============================== Get Cursor ==============================
    def get_cursor(self, event=""):
       try:
           cursor_focus = self.student_table.focus()
           content = self.student_table.item(cursor_focus)
           data = content["values"]
          
           if data:
               # Match each field to its correct position based on INSERT order in add_data method
               self.var_dep.set(data[0])          # Department
               self.var_course.set(data[1])       # Course
               self.var_year.set(data[2])         # Year
               self.var_semester.set(data[3])     # Semester
               self.var_std_id.set(data[4])       # StudentId
               self.var_std_name.set(data[5])     # Name
               self.var_div.set(data[6])          # Division
               self.var_roll.set(data[13])        # Roll No. (fixed position)
               self.var_gender.set(data[14])      # Gender (fixed position)
               self.var_dob.set(data[7])          # DOB
               self.var_email.set(data[8])        # Email
               self.var_phone.set(data[9])        # Phone
               self.var_address.set(data[10])     # Address
               self.var_teacher.set(data[11])     # Teacher
               self.var_radio1.set(data[12])      # PhotoSampleStatus
       except Exception as e:
           print(f"Error in get_cursor: {e}")



# ======================= UPDATE FUNCTION =======================
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required")
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update the Student Details", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Assehgal1@", database="face_recognization_system")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "UPDATE Student SET Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll_No=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_ID=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()
                        )
                    )
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student Details successfully updated", parent=self.root)
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    
    
    # ======================== DELETE FUNCTION ==========================
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student data", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Assehgal1@", database="face_recognization_system")
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM student WHERE Student_ID = %s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete", "Successfully Deleted student details", parent=self.root)
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    
    # ======================== RESET FUNCTION ==========================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    
    # =================== FACE CROP FUNCTION ===========================
    def face_crop(self, img):
        face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(grey, 1.3, 5)
        for (x, y, w, h) in faces:
            face_cropped = img[y:y + h, x:x + w]
            return face_cropped
        return None  # If no face found, return None
    
    # ================ GENERATE DATASET FUNCTION =======================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
            return
    
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Assehgal1@", database="face_recognization_system")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            my_result = my_cursor.fetchall()
    
            # Use the existing student ID directly (don't use id = count+1 logic)
            student_id = self.var_std_id.get()
    
            my_cursor.execute(
                "UPDATE Student SET Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll_No=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_ID=%s",
                (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    "Yes",
                    student_id
                )
            )
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()
    
            # Start capturing face data
            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, my_frame = cap.read()
                if ret:
                    cropped_face = self.face_crop(my_frame)
                    if cropped_face is not None:
                        img_id += 1
                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(student_id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)
    
                    if cv2.waitKey(1) == 13 or img_id == 100:  # Press 'Enter' or collect 100 images
                        break
    
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Generating Dataset Completed", parent=self.root)
    
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    
        
        
    
    
    



if __name__ == "__main__":
    root = Tk()
    obj = student_details(root)

    root.mainloop()
