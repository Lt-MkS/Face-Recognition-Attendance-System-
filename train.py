# traing the model : Uing LBP pattern to train
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1284x760")  # Match to image size
        self.root.title("Student Details")
        title_lbl = Label(self.root, text="Train Data Set", font=("time new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1330, height=50)
        # Top Image
        img_top = Image.open("photos/face_scan.png")
        img_top = img_top.resize((1300, 350), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        top_label = Label(self.root, image=self.photoimg_top)
        top_label.place(x=0, y=50, width=1284, height=280)

        # Bottom Image
        img_bottom = Image.open("photos/face_scan.png")
        img_bottom = img_bottom.resize((1300, 350), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        bottom_label = Label(self.root, image=self.photoimg_bottom)
        bottom_label.place(x=0, y=400, width=1284, height=300)

        # Center Button
        b1 = Button(self.root, cursor="hand2",text="Train Data",command=self.train_classifier, font=("time new roman",20,"bold"),bg="white",fg="red")
        b1.place(x=0, y=330, width=1284, height= 80)
    
    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[] 
        ids=[]
        for image in path:
            img = Image.open(image).convert('L') # Convert it into greyscale
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)
        # ================= Train the Classifier =================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed Successfully")
        



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)

    root.mainloop()
