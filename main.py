from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student_deta import student_details
from attendance import Attendance
import os
from train import Train
from face_recognition import face_Recognition
from developer import Developer
from help import Help
class face_recognization_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1284x760")  # Match to image size
        self.root.title("Face Recognization System")

        # Header Image
        img1 = Image.open("photos\header.jpg")
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
        title_lbl = Label(bg_label, text="Face Recognization Attendance System", font=("time new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1330, height=50)

        # Coordinates
        start_x = 100
        button_width = 220
        spacing = 80

        # Student Button 
        img4 = Image.open("photos/student.jpg")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_label,command=self.student_det, image=self.photoimg4, cursor="hand2")
        b1.place(x=start_x, y=100, width=220, height=220)
        b1_1 = Button(bg_label,command=self.student_det, text="Student Details", cursor="hand2", font=("time new roman", 15, "bold"), bg="white", fg="red")
        b1_1.place(x=start_x, y=320, width=220, height=40)

        # Face recognization Button
        img5 = Image.open("photos/face_detection.jpg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b2 = Button(bg_label, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b2.place(x=start_x + (button_width + spacing), y=100, width=220, height=220)
        b2_2 = Button(bg_label, text="Face Detection", cursor="hand2",command=self.face_data, font=("time new roman", 15, "bold"), bg="white", fg="red")
        b2_2.place(x=start_x + (button_width + spacing), y=320, width=220, height=40)

        # Attendance Button
        img6 = Image.open("photos/attendance.png")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b3 = Button(bg_label, image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        b3.place(x=start_x + 2 * (button_width + spacing), y=100, width=220, height=220)
        b3_3 = Button(bg_label, text="Attendance", cursor="hand2",command=self.attendance_data, font=("time new roman", 15, "bold"), bg="white", fg="red")
        b3_3.place(x=start_x + 2 * (button_width + spacing), y=320, width=220, height=40)

        # Help Desk Button
        img7 = Image.open("photos/help_desk.png")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)  # ← fixed reuse bug, added new variable
        b4 = Button(bg_label, image=self.photoimg7, cursor="hand2",command=self.help_data)
        b4.place(x=start_x + 3 * (button_width + spacing), y=100, width=220, height=220)
        b4_4 = Button(bg_label, text="Help Desk", cursor="hand2", command=self.help_data,font=("time new roman", 15, "bold"), bg="white", fg="red")
        b4_4.place(x=start_x + 3 * (button_width + spacing), y=320, width=220, height=40)

         # Train Face Button
        img8 = Image.open("photos/train.png")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)  # ← fixed reuse bug, added new variable
        b5 = Button(bg_label, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b5.place(x=start_x , y=365, width=220, height=220)
        b5_5 = Button(bg_label, text="Train Face", cursor="hand2",command=self.train_data, font=("time new roman", 15, "bold"), bg="white", fg="red")
        b5_5.place(x=start_x , y=550, width=220, height=40)
  
          # Photo Face Button
        img9 = Image.open("photos/photos.png")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)  # ← fixed reuse bug, added new variable
        b6 = Button(bg_label, image=self.photoimg9, cursor="hand2",command= self.open_img)
        b6.place(x=start_x + 300, y=365, width=220, height=220)
        b6_6 = Button(bg_label, text="Photos", cursor="hand2",command= self.open_img, font=("time new roman", 15, "bold"), bg="white", fg="red")
        b6_6.place(x=start_x +300 , y=550, width=220, height=40)
  
           # Developers
        img10 = Image.open("photos/developers.png")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)  # ← fixed reuse bug, added new variable
        b7 = Button(bg_label, image=self.photoimg10, cursor="hand2",command=self.developer_data)
        b7.place(x=start_x + 600, y=365, width=220, height=220)
        b7_7 = Button(bg_label, text="Developers", cursor="hand2",command=self.developer_data, font=("time new roman", 15, "bold"), bg="white", fg="red")
        b7_7.place(x=start_x +600 , y=550, width=220, height=40)


         # Exit
        img11 = Image.open("photos/exit.png")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)  # ← fixed reuse bug, added new variable
        b8 = Button(bg_label, image=self.photoimg11, cursor="hand2",command=self.exit)
        b8.place(x=start_x + 900, y=365, width=220, height=220)
        b8_8 = Button(bg_label, text="Exit", cursor="hand2", command = self.exit, font=("time new roman", 15, "bold"), bg="white", fg="red")
        b8_8.place(x=start_x +900 , y=550, width=220, height=40)

    def open_img(self):
        os.startfile("data")














### ------------------ Function Buttons ----------------------
    def student_det(self):
        self.new_window = Toplevel(self.root)
        self.app = student_details(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = face_Recognition(self.new_window)
    
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
    
    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)
    
    def exit(self):
        self.root.destroy()
 






















if __name__ == "__main__":
    root = Tk()
    obj = face_recognization_system(root)
    root.mainloop()

