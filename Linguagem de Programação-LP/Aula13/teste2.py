import pyautogui
import time

time.sleep(5)

im1=pyautogui.screenshot(region=(0,0,300,400))
im1.sang('imagem2.png')