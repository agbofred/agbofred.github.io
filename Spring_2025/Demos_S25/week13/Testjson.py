import json

with open("/Users/fjagbo/Documents/GitHub/agbofred.github.io/Spring_2025/Demos_S25/week13/dna.json") as fh:
    data = json.load(fh)
    for key, val in data.items():
        print(f"{key} ----------------------- {val}")
