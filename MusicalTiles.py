from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

colorMargin = 24;

DESIRED_RGB = [41,  77,  61] # r, g, and b

PIXEL_1 = [370, 630] # x and y
PIXEL_2 = [480, 630] # x and y
PIXEL_3 = [570, 630] # x and y
PIXEL_4 = [660, 630] # x and y

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def isRGB_Equal(x,y):
    return x[0] - y[0] <= colorMargin and x[1] - y[1] <= colorMargin and x[2] - y[2] <= colorMargin

keyboard.wait("q")
pos = pyautogui.position()
PIXEL_1[0] = pos[0]
PIXEL_1[1] = pos[1]
print("PIXEL_1 Set at",PIXEL_1)

keyboard.wait("q")
pos = pyautogui.position()
PIXEL_2[0] = pos[0]
PIXEL_2[1] = pos[1]
print("PIXEL_2 Set at",PIXEL_2)

keyboard.wait("q")
pos = pyautogui.position()
PIXEL_3[0] = pos[0]
PIXEL_3[1] = pos[1]
print("PIXEL_3 Set at",PIXEL_3)

keyboard.wait("q")
pos = pyautogui.position()
PIXEL_4[0] = pos[0]
PIXEL_4[1] = pos[1]
print("PIXEL_4 Set at",PIXEL_4)

keyboard.wait("q")
pos = pyautogui.position()
color = pyautogui.pixel(pos[0], pos[1])
DESIRED_RGB[0] = color[0]
DESIRED_RGB[1] = color[1]
DESIRED_RGB[2] = color[2]
print("Set rgb value to",DESIRED_RGB)

time.sleep(0.5)
while keyboard.is_pressed('q') == False:
    if keyboard.is_pressed('q'):
        break
    
    if isRGB_Equal(pyautogui.pixel(PIXEL_1[0],PIXEL_1[1]), DESIRED_RGB):
        click(PIXEL_1[0], PIXEL_1[1])
    if isRGB_Equal(pyautogui.pixel(PIXEL_2[0],PIXEL_2[1]), DESIRED_RGB):
        click(PIXEL_2[0], PIXEL_2[1])
    if isRGB_Equal(pyautogui.pixel(PIXEL_3[0],PIXEL_3[1]), DESIRED_RGB):
        click(PIXEL_3[0], PIXEL_3[1])
    if isRGB_Equal(pyautogui.pixel(PIXEL_4[0],PIXEL_4[1]), DESIRED_RGB):
        click(PIXEL_4[0], PIXEL_4[1])

exit()
