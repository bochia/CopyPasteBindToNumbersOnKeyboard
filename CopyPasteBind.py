from CopyBindPasteConstants import CONFIGURATION_PAGE_ID, CSS_STYLE_ATTRIBUTE, CSS_DISPLAY_BLOCK, CSS_DISPLAY_NONE, DIFFERENCE_BETWEEN_FUNCTION_KEY_AND_KEYBOARD_NUMBERS, HOW_TO_USE_PAGE_ID, MAIN_PAGE_ID
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

def CreateHotKey(copy_bind_pairs, numberKey):
    keyboard.add_hotkey(f"ctrl+c+{numberKey}", BindCopiedTextToNumberKey, args=(copy_bind_pairs, numberKey))
    keyboard.add_hotkey(f"ctrl+b+{numberKey}", PasteBindedValue, args=(copy_bind_pairs, numberKey))
    functionNumberKey = numberKey + DIFFERENCE_BETWEEN_FUNCTION_KEY_AND_KEYBOARD_NUMBERS
    keyboard.add_hotkey(f"f{functionNumberKey}", PasteBindedValue, args=(copy_bind_pairs, numberKey))

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

def openPage_configuration():
    mainPage.setAttribute(CSS_STYLE_ATTRIBUTE, CSS_DISPLAY_NONE)
    howToUsePage.setAttribute(CSS_STYLE_ATTRIBUTE, CSS_DISPLAY_NONE)
    configurationPage.setAttribute(CSS_STYLE_ATTRIBUTE, CSS_DISPLAY_BLOCK)
    print("Made it to openPage_configuration.")

def openPage_how_to_use():
    mainPage.setAttribute(CSS_STYLE_ATTRIBUTE, CSS_DISPLAY_NONE)
    howToUsePage.setAttribute(CSS_STYLE_ATTRIBUTE, CSS_DISPLAY_BLOCK)
    configurationPage.setAttribute(CSS_STYLE_ATTRIBUTE, CSS_DISPLAY_NONE)
    print("Made it to openPage_how_to_use")

def openPage_main():
    mainPage.setAttribute(CSS_STYLE_ATTRIBUTE, CSS_DISPLAY_BLOCK)
    howToUsePage.setAttribute(CSS_STYLE_ATTRIBUTE, CSS_DISPLAY_NONE)
    configurationPage.setAttribute(CSS_STYLE_ATTRIBUTE, CSS_DISPLAY_NONE)
    print("Made it to openPage_main.")

def PasteBindedValue(copy_bind_pairs, numberKey):
    pyperclip.copy(copy_bind_pairs[numberKey])
    keyboard.press_and_release("ctrl+v")    

########### Main Program ########### 
CreateHotKeys()

try:
    win = Neutron.Window("Copy Paste Bind Running...", css="css\style.css")

    win.display(file="html\MainWindow.html")

    win.getElementById("mainMenuButton").addEventListener("click", Neutron.event(openPage_main))
    win.getElementById("howToUsePageMenuButton").addEventListener("click", Neutron.event(openPage_how_to_use))
    win.getElementById("configurationMenuButton").addEventListener("click", Neutron.event(openPage_configuration))

    mainPage = win.getElementById(MAIN_PAGE_ID)
    howToUsePage = win.getElementById(HOW_TO_USE_PAGE_ID)
    configurationPage = win.getElementById(CONFIGURATION_PAGE_ID)
    
    win.show()

    sys.exit(0)

except Exception as e:
    easygui.msgbox("Oops something went wrong...\n\nException:\n" + str(e))