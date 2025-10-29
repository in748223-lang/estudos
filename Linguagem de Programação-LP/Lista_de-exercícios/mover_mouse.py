import pyautogui
import time

for i in range(5):
    x, y = pyautogui.position()
    print(f"Posição do mouse: X={x}, Y={y}")
time.sleep(1)