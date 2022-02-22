from time import sleep
import keyboard
import pyperclip

def SaveCopiedTextToList(copy_bind_values, key):
    keyboard.press_and_release("ctrl+c")
    value = pyperclip.paste()
    copy_bind_values[key] = value

def PasteValue(copy_bind_pairs, key):
    pyperclip.copy(copy_bind_pairs[key])
    keyboard.press_and_release("ctrl+v")

def CreateHotKey(copy_bind_pairs, numberKey):
    keyboard.add_hotkey(f"ctrl+c+{numberKey}", SaveCopiedTextToList, args=(copy_bind_pairs, numberKey))
    keyboard.add_hotkey(f"ctrl+b+{numberKey}", PasteValue, args=(copy_bind_pairs, numberKey))


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




#Main
CreateHotKeys()

while True:  
    try:
        sleep(2)
    except:
        break