# import math
'''Run the script and open paint within 9 seconds and place mouse pointer at the center'''
import pyautogui
import time
print('Drawing starts in 9 seconds...')
# open paint in 9 seconds
time.sleep(9)
distance = 200
while distance > 0:
        pyautogui.drag(distance, 0, duration=0.5)   # move right
        distance -= 5
        pyautogui.drag(0, distance, duration=0.5)   # move down
        pyautogui.drag(-distance, 0, duration=0.5)  # move left
        distance -= 5
        pyautogui.drag(0, -distance, duration=0.5)  # move up


