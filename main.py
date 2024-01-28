import sys 
import json
import clipboard

SAVED_DATA = "clipboard.json"

def save_json(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)
    
def load_json(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
       return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_json(SAVED_DATA)

    if command == "/save":
        key = input("enter a uniq key: ")
        data[key] = clipboard.paste()

        save_json(SAVED_DATA, data)
    elif command == "/load":
        key = input("Key: ")

        if key in data:
            clipboard.copy(data[key])
        else:
            print("Invalid Key")

    elif command == "/list":
        print(data)
    else:
        print(f"there is no internal command called \"{command}\"")

elif len(sys.argv) != 2:
    print("Exceed the number of allowed commads")
else:
    print("no command availabel")
