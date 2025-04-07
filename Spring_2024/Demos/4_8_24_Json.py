import json

with open("DNS.json") as fh:
    data = json.load(fh)
    for key, value in data.items():
        print(f'{key} >>>>> {value} \n')