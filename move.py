import pyautogui, sys
import time, random

#for i in range(500):
while(True):
    x = random.randint(0,500)
    y = random.randint(0,500)
    pyautogui.moveTo(x,y)
    #pyautogui.rightClick()
    print("moving..")
    time.sleep(8)

