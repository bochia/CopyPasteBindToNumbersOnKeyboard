from time import sleep
import keyboard

def SaveCopiedTextToList(copy_bind_values, key, value):
    copy_bind_values[key] = value

def PrintValue(key):
    # print("adfadfasdf")
    print(copy_bind_pairs[key])

def CreateHotKey(numberKey):
    keyboard.add_hotkey("ctrl+c+1", SaveCopiedTextToList, args=(copy_bind_pairs, 1, "copy bind value 1"))
    keyboard.add_hotkey("ctrl+b+2", PrintValue, args=([1]))

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

# keyboard.add_hotkey("ctrl+c+1", SaveCopiedTextToList, args=(copy_bind_pairs, 1, "copy bind value 1"))
# keyboard.add_hotkey("ctrl+b+2", PrintValue, args=([1]))


while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        sleep(2)
        pass
    except:
        break  # if user pressed a key other than the given key the loop will break