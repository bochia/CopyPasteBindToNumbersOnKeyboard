from logging import exception
from time import sleep
import keyboard
import pyperclip
import easygui
import sys

########### Functions ########### 
def BindCopiedTextToNumberKey(copy_bind_values, key):
    keyboard.press_and_release("ctrl+c")
    value = pyperclip.paste()
    copy_bind_values[key] = value

def PasteBindedValue(copy_bind_pairs, key):
    pyperclip.copy(copy_bind_pairs[key])
    keyboard.press_and_release("ctrl+v")

def CreateHotKey(copy_bind_pairs, numberKey):
    keyboard.add_hotkey(f"ctrl+c+{numberKey}", BindCopiedTextToNumberKey, args=(copy_bind_pairs, numberKey))
    keyboard.add_hotkey(f"ctrl+b+{numberKey}", PasteBindedValue, args=(copy_bind_pairs, numberKey))
    keyboard.add_hotkey(f"ctrl+{numberKey}", PasteBindedValue, args=(copy_bind_pairs, numberKey))

def CreateHotKeys():

    copy_bind_pairs = {
        0:"",
        1:"",
        2:"",
        3:"",
        4:"",
        5:"",
        6:"",
        7:"",
        8:"",
        9:""
    }

    for numberKey in range(0,9):
        CreateHotKey(copy_bind_pairs, numberKey)

########### Main Program ########### 
CreateHotKeys()

try:
    msg = "HOW TO USE:\n"
    msg += "-----------\n\n"
    msg += "Bind Text To Number: ctrl + c + {number key}" + "\n\n"
    msg += "Paste Binded Text: ctrl + b + {number key}\n\n"
    msg += "IMPORTANT:\n"
    msg += "----------\n"
    msg += "This window must stay open to use the CopyPasteBind feature but feel free to minimize it."

    easygui.msgbox(msg=msg, title="Copy Paste Bind Running...", ok_button="Stop Program")
    sys.exit(0)
        
except Exception as e:
    easygui.msgbox("Oops something went wrong...\n\nException:\n" + str(e))