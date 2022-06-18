from logging import exception
from time import sleep
from CopyBindPasteConstants import DIFFERENCE_BETWEEN_FUNCTION_KEY_AND_KEYBOARD_NUMBERS
import keyboard
import pyperclip
import easygui
import sys
import Neutron


########### Functions ########### 
def BindCopiedTextToNumberKey(copy_bind_values, numberKey):
    keyboard.press_and_release("ctrl+c")
    value = pyperclip.paste()
    copy_bind_values[numberKey] = value

def PasteBindedValue(copy_bind_pairs, numberKey):
    pyperclip.copy(copy_bind_pairs[numberKey])
    keyboard.press_and_release("ctrl+v")

def CreateHotKey(copy_bind_pairs, numberKey):
    keyboard.add_hotkey(f"ctrl+c+{numberKey}", BindCopiedTextToNumberKey, args=(copy_bind_pairs, numberKey))
    keyboard.add_hotkey(f"ctrl+b+{numberKey}", PasteBindedValue, args=(copy_bind_pairs, numberKey))
    keyboard.add_hotkey(f"ctrl+{numberKey}", PasteBindedValue, args=(copy_bind_pairs, numberKey))
    functionNumberKey = numberKey + DIFFERENCE_BETWEEN_FUNCTION_KEY_AND_KEYBOARD_NUMBERS
    keyboard.add_hotkey(f"f{functionNumberKey}", BindCopiedTextToNumberKey, args=(copy_bind_pairs, numberKey))

def CreateHotKeys():

    #dictionary used to save values for copy binded text.
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


def setName():
    name = win.getElementById("inputName").value
    win.getElementById("title").innerHTML = "Hello: " + name

########### Main Program ########### 
CreateHotKeys()

try:
    # Create instructions to display in dialog box.
    msg = "HOW TO USE:\n"
    msg += "-----------\n\n"
    msg += "Bind Text To Number - highlight the text you want to copy and then use one of the hotkeys below.\n\n"
    msg += " * ctrl + c + {number key}" + "\n\n"
    msg += " * Use function keys fn13 - fn22 to bind text to numbers 0 - 9 respectively.\n\n"
    msg += "Paste Binded Text - use one of the hotkeys below.\n\n"
    msg += " * ctrl + {number key}\n\n"
    msg += " * ctrl + b + {number key}\n\n"
    msg += "IMPORTANT:\n"
    msg += "----------\n"
    msg += "This window must stay open to use the CopyPasteBind functionality, but feel free to minimize it."

    # easygui.msgbox(msg=msg, title="Copy Paste Bind Running...", ok_button="Stop Program")
    # sys.exit(0)
    
    win = Neutron.Window("Example")


    win.display(f"""

    <!DOCTYPE html>
    <html>
    <head lang="en">
        <meta charset="UTF-8">
    </head>
    <body>
        <h1 id="title">Hello: </h1>
        <input id="inputName">
        <button id="submitName" onclick="{Neutron.event(setName)}">Submit</button>
        <!-- OR-->
        {Neutron.elements.Button(win, content="Submit", onclick=Neutron.event(setName))}
    </body>
    </html>
    """)
    win.show()

except Exception as e:
    easygui.msgbox("Oops something went wrong...\n\nException:\n" + str(e))