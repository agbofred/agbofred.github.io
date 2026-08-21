import json

with open("dnd.json") as fh:
    data = json.load(fh)
    for key, value in data.items():
        print(f"{key} ----------------> {value}")
        with open("new_jfile.json", "a"):
            if value:
                d={key: value}
                json.dump(d, fh)
           