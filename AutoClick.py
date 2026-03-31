import time
import keyboard
import random
from pynput.keyboard import Key, Controller
import win32api, win32con
import threading

#####
ExitWhenDone = False
#####

isRunning = False

class check (threading.Thread):
    def __init__(self, key):
        threading.Thread.__init__(self)
        self.key = key
    def run(self):
        def close(e):
            global isRunning
            if isRunning:
                isRunning = False
        
        keyboard.on_press_key(self.key, close)

def Main():
    global isRunning
    isRunning = False
    
    keyboard.wait("z")
    time.sleep(0.5)
    
    isRunning = True

    t = check('z')
    t.start()
    
    while isRunning:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.005)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.005)

    if ExitWhenDone:
        exit()
    else:
        Main()

Main()
