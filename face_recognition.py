from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1284x760")  # Match to image size
        self.root.title("Student Face Recognition")
    # Title
        title_lbl = Label(self.root, text="Face Recognization", font=("time new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1330, height=50)
    # Image left
        img_left = Image.open("photos/image_left.png")
        img_left = img_left.resize((500, 600), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        left_label = Label(self.root, image=self.photoimg_left)
        left_label.place(x=0, y=50, width=500, height=600)
    # Image right
        img_right = Image.open("photos/right_image.png")
        img_right = img_right.resize((780, 600), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        right_label = Label(self.root, image=self.photoimg_right)
        right_label.place(x=500, y=50, width=780, height=600)
    # Button
        b1 = Button(self.root, cursor="hand2",text="Recognize Face",command=self.face_recog, font=("time new roman",15,"bold"),bg="white",fg="darkgreen")
        b1.place(x=792, y=579, width=250, height= 40)

    # ====================== Attendance =======================
    def mark_attendance(self,i,r,n,d):
        with open("Attendance_list.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

                




    
    #======================== Face Recognition ========================
    def face_recog(self):
        def draw_boundary(img, classifier, scalefactor, minNeighbour, color, text, clf):
            # ✅ Check if image is loaded
            if img is None:
                print("Error: Image is empty")
                return []  # Return empty list or handle as needed
    
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scalefactor, minNeighbour)
            coord = []
    
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))
                conn = mysql.connector.connect(host="localhost", username="root", password="Assehgal1@", database="face_recognization_system")
                my_cursor = conn.cursor()
    
                # Name
                my_cursor.execute("select Name from student where Student_ID =" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n) if n else "Unknown"
    
                # Roll_No
                my_cursor.execute("select Roll_No from student where Student_ID =" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "Unknown"
    
                # Department
                my_cursor.execute("select Department from student where Student_ID =" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d) if d else "Unknown"

                # Student ID
                my_cursor.execute("select Department from student where Student_ID =" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i) if i else "Unknown"
    
                if confidence > 77:
                    cv2.putText(img, f"ID: {i}", (x, y - 70), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll No : {r}", (x, y - 50), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name : {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department : {d}", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
    
                coord = [x, y, w, h]
            return coord
    
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img
    
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
    
        video_cap = cv2.VideoCapture(0)
    
        while True:
            ret, img = video_cap.read()
            if not ret:  # ✅ Check if frame was successfully read
                print("Failed to grab frame from camera")
                continue  # or break
    
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)
    
            if cv2.waitKey(1) == 13:  # Enter key to exit
                break
    
        video_cap.release()
        cv2.destroyAllWindows()
    
    

if __name__ == "__main__":
    root = Tk()
    obj = face_Recognition(root)

    root.mainloop()
