import cv2
import pyautogui
from hand_tracking import HandTracker
from cursor_control import CursorController

# Initialize webcam
cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()

# Initialize hand tracker and cursor controller
hand_tracker = HandTracker()
cursor_controller = CursorController(screen_width, screen_height)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)  # Mirror the camera
    results = hand_tracker.find_hands(frame)
    hand_tracker.draw_hands(frame, results)
    
    landmarks = hand_tracker.get_landmarks(results)

    if landmarks:
        index_finger = landmarks[8]  # Index finger tip
        cursor_controller.move_cursor(index_finger[0], index_finger[1])

        # Thumb and index finger tip distance for clicking
        thumb_tip = landmarks[4]
        distance = ((thumb_tip[0] - index_finger[0]) ** 2 + (thumb_tip[1] - index_finger[1]) ** 2) ** 0.5

        if distance < 0.05:
            cursor_controller.click()

    cv2.imshow("AirCursor", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
