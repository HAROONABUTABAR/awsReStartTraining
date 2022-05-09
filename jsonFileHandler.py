import json
import jsonFileHandler

def readJsonFile(jsonFileHandler):
    data = ""
    try:
        with open('/awsReStartTraining/insulin.json') as json_file:
            data = json.load(jsonFileHandler)
    except IOError:
        print("Could not read file")
    return data