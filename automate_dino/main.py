import pyautogui
import time
from PIL import Image, ImageGrab

def play():
    image = ImageGrab.grab().convert('L')
    content = image.load()
    for i in range(160, 250):
        for j in range(410, 490):
            content[i, j] = 150
                # pyautogui.keyDown('up')
    image.show()

if __name__ == "__main__":
    print('Starts in 6 seconds...')
    time.sleep(3)
    pyautogui.keyDown('up')
    # while True:
    #     image = ImageGrab.grab().convert('L')
    #     content = image.load()
    #     for i in range(160, 250):
    #         for j in range(400, 490):
    #             if content[i, j] > 150:
    #                 pyautogui.keyDown('up')
    # image.show()
    #     break
    play()

