from win32api import keybd_event,SetCursorPos,mouse_event
from win32con import KEYEVENTF_KEYUP,MOUSEEVENTF_LEFTDOWN,MOUSEEVENTF_LEFTUP
from win32gui import GetWindowRect,FindWindow
import keyboard
import time
time.sleep(5)
hwnd = FindWindow('ConsoleWindowClass','C:\Windows\system32\cmd.exe')
local = GetWindowRect(hwnd)
x = int((local[0]+local[2]/2)/2)
y = int((local[1]+local[3]/2)/2)
SetCursorPos([x,y])
mouse_event(MOUSEEVENTF_LEFTDOWN,x,y,0,0)
mouse_event(MOUSEEVENTF_LEFTUP,x,y,0,0)
paths =r"C:\Users\admin\Desktop\lab.py"
path = paths.upper()
def inp(ass):
    keybd_event(ass,0,0,0)
    keybd_event(ass,0,KEYEVENTF_KEYUP,0)
    time.sleep(0.01)
for i in path:
    if i == ':':
        keybd_event(16, 0, 0, 0)
        keybd_event(186, 0, 0, 0)
        keybd_event(186, 0, KEYEVENTF_KEYUP, 0)
        keybd_event(16, 0, KEYEVENTF_KEYUP, 0)
        continue
    a = int(keyboard.dicr[i])
    inp(a)
inp(ord("\r"))
inp(ord("\n"))
QWE = input("")
