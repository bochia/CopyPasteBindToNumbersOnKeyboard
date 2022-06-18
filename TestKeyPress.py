import keyboard
from time import sleep

while True:
    print(keyboard.read_hotkey())
    sleep(2)
