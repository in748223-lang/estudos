import pyautogui
import time 

pyautogui.press("win")
pyautogui.write("chorme")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("wikipedia")
pyautogui.press("enter")
pyautogui.click(x = 1092, y = 342,duration =1)