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

def addStartup():  # this will add the file to the startup registry key
    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = sys.argv[0].split('\\')[-1]
    new_file_path = fp + '\\' + file_name
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    SetValueEx(key2change, 'AutoAccceptLoL', 0, REG_SZ,
               new_file_path)

def Hide():
    import win32console
    import win32gui
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)

addStartup()

Hide()

while True:
    try:
        acc = \
            pyautogui.locateOnScreen(
                'accept.PNG',
                confidence=.7
            )
        acc_co = pyautogui.center(acc)
        x,y = acc_co.x, acc_co.y
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
    except:
        time.sleep(1)
