# Facial-recognition-
This project is a simple face recognition system built with Python, OpenCV, and the face_recognition library. It detects faces in images, compares them with known faces, and highlights matches with names. Easy to use, customizable, and great for learning computer vision basics.
🔍 Face Recognition System using Python

A simple and efficient Face Recognition System built using Python, OpenCV, and the face_recognition library.
This project detects and recognizes faces by comparing unknown images with a set of known faces.

🚀 Features

📂 Load and encode known faces from a directory

🧠 Detect faces in unknown images

🔎 Compare faces using configurable tolerance

🟢 Draw bounding boxes around recognized faces

🏷️ Display the matched person's name on the image

⚡ Uses HOG model for fast face detection

🛠️ Tech Stack

Python

OpenCV

face_recognition (dlib-based)

NumPy

📁 Project Structure
project/
│
├── known face/        # Store known face images (named as person.jpg)
├── unknown face/      # Store images to test
├── face.py            # Main script
└── README.md
⚙️ How It Works

The system loads all images from the "known face" folder.

It extracts face encodings and stores them.

It scans images from the "unknown face" folder.

Faces are detected and compared with known encodings.

If a match is found:

A green rectangle is drawn around the face.

The matched name is displayed below it.

🧪 How to Run
1️⃣ Install Dependencies
pip install face_recognition opencv-python numpy
2️⃣ Add Images

Add labeled images in known face/

Add test images in unknown face/

3️⃣ Run the Script
python face.py
🎯 Configuration

You can adjust these parameters in face.py:

TOLERANCE = 0.6   # Lower = stricter matching
MODEL = "hog"     # hog (fast) or cnn (more accurate but slower)
📌 Future Improvements

Real-time webcam face recognition

Attendance system integration

Database-based face storage

GUI interface

Deploy as a web app

📷 Example Use Cases

Smart Attendance System

Security & Access Control

Identity Verification

AI-based Monitoring Systems
........
