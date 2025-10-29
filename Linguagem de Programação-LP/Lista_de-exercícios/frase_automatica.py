import pyautogui
import time
import os

# Abre o bloco de notas
os.system("notepad")
time.sleep(2)

pyautogui.write("Automatizando com PyAutoGUI é divertido!",interval=0.05)