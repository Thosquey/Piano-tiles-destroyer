import keyboard
import pyautogui
import win32api, win32con
import time

BLACK = (0, 0, 0)
HORIZONTAL_VALUES = [580, 680, 780, 880]

def click(xPos: int, yPos: int) -> tuple:
    win32api.SetCursorPos((xPos, yPos))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

time.sleep(1)

while not keyboard.is_pressed('esc'):
    for X_COORD in HORIZONTAL_VALUES:
        if pyautogui.pixel(X_COORD, 200) == BLACK:
            click(X_COORD, 200)
