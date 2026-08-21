import json

with open("/Users/fjagbo/Documents/GitHub/agbofred.github.io/Spring_2024/Demos/DNS.json") as fh:
    data = json.load(fh)
    for key, value in data.items():
        print(f'{key} >>>>> {value} \n')