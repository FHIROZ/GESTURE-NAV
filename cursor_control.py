import pyautogui
import numpy as np

class CursorController:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def move_cursor(self, landmark_x, landmark_y):
        x = np.interp(landmark_x, [0.1, 0.9], [0, self.screen_width])
        y = np.interp(landmark_y, [0.1, 0.9], [0, self.screen_height])
        pyautogui.moveTo(x, y)

    def click(self):
        pyautogui.click()
