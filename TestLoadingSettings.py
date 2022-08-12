import json

with open("settings\settings.json") as json_file:
    settings = json.load(json_file)
    print(settings)
    savedValues = settings["savedValues"]
    print(savedValues)