# 📸 Facial Recognition Attendance System

An automated attendance management system using facial recognition technology. This system detects and recognizes faces in real-time using a webcam, and marks attendance by storing recognized individuals' names along with a timestamp.

---

## 🚀 Features

- 🔍 Real-time face detection using OpenCV and Haar Cascades
- 🧠 Face recognition using LBPH (Local Binary Patterns Histogram)
- 📝 Attendance logging with name, date, and time
- 💾 Stores and updates attendance in CSV file format
- 👤 Easy-to-add new users via face image registration

---

## 📂 Project Structure

```

Facial-Recognition-System/
│
├── Attendance.csv               # Attendance records
├── haarcascade\_frontalface.xml # Haar Cascade file for face detection
├── face\_dataset.py              # Captures face images for new users
├── train\_model.py               # Trains the recognition model
├── recognize.py                 # Runs the real-time attendance system
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies

````

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Facial-Recognition-System.git
cd Facial-Recognition-System
````

2. Install required libraries:

```bash
pip install -r requirements.txt
```

---

## 🎮 How to Use

### 1. Register a New User

Run the following to capture face images for a new user:

```bash
python face_dataset.py
```

### 2. Train the Recognition Model

After collecting data:

```bash
python train_model.py
```

### 3. Start Attendance System

Launch the real-time recognition system:

```bash
python recognize.py
```

> Attendance will be recorded in `Attendance.csv`

---

## 🛠️ Built With

* Python 3.x
* OpenCV
* Numpy
* CSV for attendance logging

---

## 📌 Future Enhancements

* GUI interface using Tkinter or Streamlit
* Integration with cloud or database systems
* Email or SMS notifications
* Mobile app integration

---

## 🙌 Contributing

Feel free to fork the repo, submit issues or pull requests to improve the system.

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---

## 👤 Author

Created by [Sahil Kumar](https://github.com/sahilkumar-1234)

```

---

Let me know if you want a **Streamlit version**, **dashboard feature**, or a resume-style summary for this project!
```
