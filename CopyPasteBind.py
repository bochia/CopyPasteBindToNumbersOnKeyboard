from time import sleep
import keyboard

def SaveCopiedTextToList(copy_bind_values, key, value):
    copy_bind_values[key] = value

def PrintValue(copy_bind_pairs, key):
    # print("adfadfasdf")
    print(copy_bind_pairs[key])

def CreateHotKey(copy_bind_pairs, numberKey):
    keyboard.add_hotkey(f"ctrl+c+{numberKey}", SaveCopiedTextToList, args=(copy_bind_pairs, numberKey, f"copy bind value {numberKey}")) #need to replace this with copied text.
    keyboard.add_hotkey(f"ctrl+b+{numberKey}", PrintValue, args=(copy_bind_pairs, numberKey))


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


CreateHotKeys()

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        sleep(2)
    except:
        break  # if user pressed a key other than the given key the loop will break