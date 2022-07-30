from CopyBindPasteConstants import BINDED_VALUE_TEXTBOX_PREFIX, CONFIGURATION_PAGE_ID, CSS_STYLE_ATTRIBUTE, CSS_DISPLAY_BLOCK, CSS_DISPLAY_NONE, DIFFERENCE_BETWEEN_FUNCTION_KEY_AND_KEYBOARD_NUMBERS, EMPTY_STR, HOW_TO_USE_PAGE_ID, MAIN_PAGE_ID
import keyboard
import pyperclip
import easygui
import sys
import Neutron
import os


########### Functions ########### 
def BindCopiedTextToNumberKey(copy_bind_values, numberKey):
    #copy value from clipboard and bind to number
    keyboard.press_and_release("ctrl+c")
    value = pyperclip.paste()
    copy_bind_values[numberKey] = value

    # update UI
    win.getElementById(f"{BINDED_VALUE_TEXTBOX_PREFIX}{numberKey}").innerHTML = value.replace('\n', ' ').replace('\r', '') # need to remove new line characters otherwise wont work.

def CreateHotKey(copy_bind_pairs, numberKey):
    keyboard.add_hotkey(f"ctrl+c+{numberKey}", BindCopiedTextToNumberKey, args=(copy_bind_pairs, numberKey))
    keyboard.add_hotkey(f"ctrl+b+{numberKey}", PasteBindedValue, args=(copy_bind_pairs, numberKey))
    functionNumberKey = numberKey + DIFFERENCE_BETWEEN_FUNCTION_KEY_AND_KEYBOARD_NUMBERS
    keyboard.add_hotkey(f"f{functionNumberKey}", PasteBindedValue, args=(copy_bind_pairs, numberKey))

def CreateHotKeys(copy_bind_pairs):
    for numberKey in range(0,10):
        CreateHotKey(copy_bind_pairs, numberKey)  

def hide_page(page):
    page.setAttribute(CSS_STYLE_ATTRIBUTE, CSS_DISPLAY_NONE)

def openPage_configuration():
    show_page_and_hide_all_others(CONFIGURATION_PAGE_ID)
    print("Made it to openPage_configuration.")

def openPage_how_to_use():
    show_page_and_hide_all_others(HOW_TO_USE_PAGE_ID)
    print("Made it to openPage_how_to_use")

def openPage_main():
    show_page_and_hide_all_others(MAIN_PAGE_ID)
    print("Made it to openPage_main.")

def PasteBindedValue(copy_bind_pairs, numberKey):
    pyperclip.copy(copy_bind_pairs[numberKey])
    keyboard.press_and_release("ctrl+v")    

def reset_values():
    for numKey in range(0, 10):
        copy_bind_pairs[numKey] = EMPTY_STR
        win.getElementById(f"{BINDED_VALUE_TEXTBOX_PREFIX}{numKey}").innerHTML = EMPTY_STR

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        if sys._MEIPASS2 != EMPTY_STR:
            base_path = sys._MEIPASS
        else:
            print("made it here")
            base_path = os.getcwd()
            return os.path.join(base_path, relative_path)
    except Exception:
        base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

def show_page(page):
    page.setAttribute(CSS_STYLE_ATTRIBUTE, CSS_DISPLAY_BLOCK)

def show_page_and_hide_all_others(page_Id):
    show_page(win.getElementById(page_Id))
    
    page_Ids_to_hide = [x for x in all_page_Ids if x != page_Id]

    for page_Id_to_hide in page_Ids_to_hide:
        page = win.getElementById(page_Id_to_hide)
        hide_page(page)

########### Main Program ########### 

# dictionary used to save values for copy binded text.
copy_bind_pairs = {
    0:EMPTY_STR,
    1:EMPTY_STR,
    2:EMPTY_STR,
    3:EMPTY_STR,
    4:EMPTY_STR,
    5:EMPTY_STR,
    6:EMPTY_STR,
    7:EMPTY_STR,
    8:EMPTY_STR,
    9:EMPTY_STR
}

CreateHotKeys(copy_bind_pairs)

try:
    css_filename = "style.css"
    css_filepath = EMPTY_STR
    html_filename = "MainWindow.html"
    html_filepath = EMPTY_STR

    css_filepath = f"css\{css_filename}"
    html_filepath = f"html\{html_filename}"

    css_filepath = resource_path(css_filepath)
    html_filepath = resource_path(html_filepath)

    print("mdae it here asdfasdf")
    print(css_filepath)
    print(html_filepath)

    win = Neutron.Window("Copy Paste Bind Running...", css=css_filepath)

    win.display(file=html_filepath)

    win.getElementById("mainMenuButton").addEventListener("click", Neutron.event(openPage_main))
    win.getElementById("howToUsePageMenuButton").addEventListener("click", Neutron.event(openPage_how_to_use))
    win.getElementById("configurationMenuButton").addEventListener("click", Neutron.event(openPage_configuration))
    win.getElementById("resetValues").addEventListener("click", Neutron.event(reset_values))

    mainPage = win.getElementById(MAIN_PAGE_ID)
    howToUsePage = win.getElementById(HOW_TO_USE_PAGE_ID)
    configurationPage = win.getElementById(CONFIGURATION_PAGE_ID)

    all_page_Ids = [MAIN_PAGE_ID, HOW_TO_USE_PAGE_ID, CONFIGURATION_PAGE_ID]
    
    win.show()

    sys.exit(0)

except Exception as e:
    easygui.msgbox("Oops something went wrong...\n\nException:\n" + str(e))