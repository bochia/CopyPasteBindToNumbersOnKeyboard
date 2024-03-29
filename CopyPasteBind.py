from CopyBindPasteConstants import BINDED_VALUE_TEXTBOX_PREFIX, CSS_STYLE_ATTRIBUTE, CSS_DISPLAY_BLOCK, CSS_DISPLAY_NONE, DIFFERENCE_BETWEEN_FUNCTION_KEY_AND_KEYBOARD_NUMBERS, EMPTY_STR, HOW_TO_USE_PAGE_ID, MAIN_PAGE_ID
import keyboard
import pyperclip
import easygui
import sys
import Neutron
import os
import json


########### Functions ########### 
def BindCopiedTextToNumberKey(copy_bind_values, numberKey):
    #copy value from clipboard and bind to number
    keyboard.press_and_release("ctrl+c")
    value = pyperclip.paste()
    copy_bind_values[numberKey] = value

    # update UI
    win.getElementById(f"{BINDED_VALUE_TEXTBOX_PREFIX}{numberKey}").innerHTML = remove_newline_and_return_characters(value)

def CreateHotKey(copy_bind_pairs, numberKey):
    hotkey = f"ctrl+c+{numberKey}"
    keyboard.add_hotkey(hotkey, BindCopiedTextToNumberKey, args=(copy_bind_pairs, numberKey))
    PrintHotKeyAdded(hotkey)

    hotkey = f"ctrl+b+{numberKey}"
    keyboard.add_hotkey(hotkey, PasteBindedValue, args=(copy_bind_pairs, numberKey))
    PrintHotKeyAdded(hotkey)

    functionNumberKey = numberKey + DIFFERENCE_BETWEEN_FUNCTION_KEY_AND_KEYBOARD_NUMBERS
    hotkey = f"f{functionNumberKey}"
    keyboard.add_hotkey(hotkey, PasteBindedValue, args=(copy_bind_pairs, numberKey))
    PrintHotKeyAdded(hotkey)

def CreateHotKeys(copy_bind_pairs):
    print("Attempting to create hotkeys...")

    for numberKey in range(0,10):
        CreateHotKey(copy_bind_pairs, numberKey)
    
    print("Successfully created all hotkeys.")

def hide_page(page):
    page.setAttribute(CSS_STYLE_ATTRIBUTE, CSS_DISPLAY_NONE)

def load_saved_values():
    print("Attempting to load saved values...")

    if window_has_started:
        # load saved values from settings file
        with open("settings\settings.json") as json_file:
            settings = json.load(json_file)
            savedValues = settings["savedValues"]

            #get value from settings and populate on page.
            for numberKey in range (0, 10):
                savedValue = savedValues[f"{numberKey}"]
                copy_bind_pairs[numberKey] = savedValue
                win.getElementById(f"bindValue{numberKey}").innerHTML = remove_newline_and_return_characters(savedValue)

    print("Successfully loaded saved values.")

def openPage_how_to_use():
    show_page_and_hide_all_others(HOW_TO_USE_PAGE_ID)
    print("Opened Main Page.")

def openPage_main():
    show_page_and_hide_all_others(MAIN_PAGE_ID)
    print("Opened Main Page.")

def PasteBindedValue(copy_bind_pairs, numberKey):
    pyperclip.copy(copy_bind_pairs[numberKey])
    keyboard.press_and_release("ctrl+v")    

def PrintHotKeyAdded(hotkey):
    print(f"Added hotkey {hotkey}")

# need to remove newline characters before populating text areas otherwise text wont be visible in text area.
def remove_newline_and_return_characters(string):
    string = string.replace('\n', ' ').replace('\r', '')
    return string

def reset_values():
    print("Attempting to reset hotkeys and values...")

    print("Reseting all values.")
    for numKey in range(0, 10):
        copy_bind_pairs[numKey] = EMPTY_STR
        win.getElementById(f"{BINDED_VALUE_TEXTBOX_PREFIX}{numKey}").innerHTML = EMPTY_STR

    # Remove and redadd all hotkeys. Workaround for hotkeys not working after logging out and relogging in on windows.
    print("Removing all hotkeys")
    keyboard.unhook_all_hotkeys()

    CreateHotKeys(copy_bind_pairs)

    print("Successfully reset hotkeys and values.")    

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

def save_values():
    print("Attempting to save values...")

    try:
        filePath = "settings\settings.json"
        savedValuesKey = "savedValues"
        oldSettings = ""
        newSettings = ""

        if window_has_started:
            # load saved values from settings file
            with open(filePath) as json_file:
                oldSettings = json.load(json_file)
                savedValues = oldSettings[savedValuesKey]

                #get value from settings and populate on page.
                for numberKey in range (0, 10):
                    newSavedValue = copy_bind_pairs[numberKey]
                    savedValues[f"{numberKey}"] = newSavedValue 

                oldSettings[savedValuesKey] = savedValues
                newSettings = oldSettings
            
            with open(filePath, "w") as json_file:
                json.dump(newSettings, json_file) 

    except Exception as ex:
        print(f"Exception - {ex}")
                
    print("Successfully saved values.")

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
    0: EMPTY_STR,
    1: EMPTY_STR,
    2: EMPTY_STR,
    3: EMPTY_STR,
    4: EMPTY_STR,
    5: EMPTY_STR,
    6: EMPTY_STR,
    7: EMPTY_STR,
    8: EMPTY_STR,
    9: EMPTY_STR
}

# stores hotkeys aliases 
hotkey_aliases = []

CreateHotKeys(copy_bind_pairs)

try:
    window_has_started = False
    css_filename = "style.css"
    css_filepath = EMPTY_STR
    html_filename = "MainWindow.html"
    html_filepath = EMPTY_STR

    css_filepath = f"css\{css_filename}"
    html_filepath = f"html\{html_filename}"

    css_filepath = resource_path(css_filepath)
    html_filepath = resource_path(html_filepath)

    print(css_filepath)
    print(html_filepath)

    win = Neutron.Window("Copy Paste Bind Running...", css=css_filepath)

    win.display(file=html_filepath)

    # Menu buttons
    win.getElementById("mainMenuButton").addEventListener("click", Neutron.event(openPage_main))
    win.getElementById("howToUsePageMenuButton").addEventListener("click", Neutron.event(openPage_how_to_use))

    # Main page buttons
    win.getElementById("resetValues").addEventListener("click", Neutron.event(reset_values))
    win.getElementById("loadSavedValues").addEventListener("click", Neutron.event(load_saved_values))
    win.getElementById("saveValues").addEventListener("click", Neutron.event(save_values))

    mainPage = win.getElementById(MAIN_PAGE_ID)
    howToUsePage = win.getElementById(HOW_TO_USE_PAGE_ID)

    all_page_Ids = [MAIN_PAGE_ID, HOW_TO_USE_PAGE_ID]
    
    window_has_started = True
    win.show()

    sys.exit(0)

except Exception as ex:
    easygui.msgbox("Oops something went wrong...\n\nException:\n" + str(ex))