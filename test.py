import pyautogui
import time
import sys
from PIL import Image
import numpy

def current_position():
    while True:
        print("Current Cursor Position: ", pyautogui.position())
        time.sleep(1)

def test_move_click():
    while True:
        x, y = pyautogui.position()

        if x <= 100 and y <= 100:
            print("Moving Mouse...")
            time.sleep(1)
            pyautogui.moveTo(x=693, y=693)

            print("Clicking Mouse...")
            pyautogui.click(x=693, y=693)

if __name__ == "__main__":
    print("Start Testing...")

    current_position()




