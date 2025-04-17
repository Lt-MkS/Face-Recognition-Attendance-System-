💻 Advanced Face Recognition Attendance System using Python
📌 Project Overview
This project is an AI-powered attendance management system that uses face recognition technology to automate and simplify the process of marking attendance. Built with Python and OpenCV, the system can detect and recognize multiple faces in real-time and record attendance with timestamps — eliminating the need for manual entry or biometric devices.

🚀 Features
🎯 Real-time face detection and recognition using a webcam

🧠 Uses face_recognition / Dlib models for high-accuracy face embeddings

📅 Automatically records name, date, and time of attendance

🔄 Prevents duplicate entries within a session

🗃️ Stores attendance in CSV/Excel format

🧑‍💻 Face registration module to add new users

🖥️ Optional GUI using Tkinter for ease of use

🛠️ Technologies Used
Python

OpenCV

face_recognition / Dlib / NumPy

Pandas

Tkinter (for GUI)

CSV / Excel / SQLite (for attendance storage)

📷 How It Works
Face Registration: Register faces by capturing images via webcam.

Encoding: Convert facial features into numerical encodings using face embeddings.

Live Recognition: Compare real-time webcam feed to stored encodings.

Attendance Logging: If a match is found, log attendance with timestamp.
