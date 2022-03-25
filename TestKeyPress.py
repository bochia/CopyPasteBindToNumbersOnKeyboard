import keyboard
from time import sleep

def printText():
    print("alt key pressed")

keyboard.on_press_key("right shift", printText)

while True:
    sleep(2)
