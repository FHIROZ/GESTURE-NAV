🖐️ Hand Gesture Controlled Cursor
Control your mouse cursor using just your hand gestures!
This project uses OpenCV, MediaPipe, and PyAutoGUI to track your hand movements via webcam and translate them into real-time cursor control and click actions.

🔧 Technologies Used
Python 3

OpenCV – for capturing and displaying webcam video.

MediaPipe – for real-time hand landmark detection.

PyAutoGUI – for controlling the mouse cursor and performing clicks.

NumPy – for coordinate mapping (interpolation).

📁 Project Structure
graphql
Copy
Edit
├── main.py                # Main program to run gesture-controlled cursor
├── hand_tracking.py       # HandTracker class using MediaPipe
├── cursor_control.py      # CursorController class using PyAutoGUI
├── README.md              # Project documentation
🚀 How It Works
Webcam captures live video feed.

MediaPipe detects and tracks your hand and its key landmarks.

The tip of the index finger controls the cursor movement.

When the thumb and index finger tips come close, it simulates a mouse click.

NumPy is used to map normalized hand coordinates to screen coordinates.

PyAutoGUI moves the cursor and performs clicks on the screen.

✅ Features
Real-time hand tracking

Cursor movement using index finger

Click action using thumb-index pinch gesture

Lightweight and fast

🖥️ Requirements
Install dependencies using pip:

bash
Copy
Edit
pip install opencv-python mediapipe pyautogui numpy
▶️ How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/hand-gesture-cursor.git
cd hand-gesture-cursor
Run the main program:

bash
Copy
Edit
python main.py
Use your right hand to control the cursor:

Move your index finger to move the mouse.

Bring thumb and index finger together to click.

📸 Demo
(Add a short screen recording or GIF here to show how it works)

🧠 Inspiration
Inspired by futuristic human-computer interaction systems like Iron Man's J.A.R.V.I.S. and touchless interfaces, this project aims to explore hands-free computing using AI and computer vision.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

📜 License
This project is open-source and available under the MIT License.
