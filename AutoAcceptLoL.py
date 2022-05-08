import pyautogui
import time
from winreg import *
import sys, os
import cv2

"""
 _______  __    _               ______   _______ 
(  ____ \/  \  ( \    |\     /|/ ___  \ (  ____ )
| (    \/\/) ) | (    | )   ( |\/   \  \| (    )|
| (_____   | | | |    | |   | |   ___) /| (____)|
(_____  )  | | | |    ( (   ) )  (___ ( |     __)
      ) |  | | | |     \ \_/ /       ) \| (\ (   
/\____) |__) (_| (____/\ \  /  /\___/  /| ) \ \__
\_______)\____/(_______/ \_/   \______/ |/   \__/
                                                  
"""

# this will add the file to the startup registry, comment if you do not need it
def addStartup():  
    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = sys.argv[0].split('\\')[-1]
    new_file_path = fp + '\\' + file_name
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    SetValueEx(key2change, 'AutoAccceptLoL', 0, REG_SZ,
               new_file_path)

addStartup()

# this is the actual program
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path + "\check.png"
while True:
    try:
        acc = \
            pyautogui.locateOnScreen(
                dir_path,
                confidence=.7
                )
        acc_co = pyautogui.center(acc)
        x,y = acc_co.x, acc_co.y
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
    except:
        time.sleep(1)