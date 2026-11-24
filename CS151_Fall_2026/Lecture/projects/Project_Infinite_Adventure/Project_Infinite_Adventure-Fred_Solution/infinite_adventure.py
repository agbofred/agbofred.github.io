######################################################################
# Name:
# Collaborators:
# Section leader's name:
# Generative AI transcript (if any):
# List of extensions (if any):
######################################################################

import json
from notopenai import NotOpenAI
import os
from pgl import GWindow, GImage, GRect

# your instructor should have sent you an api key
CLIENT = NotOpenAI(api_key="your_api_key_here")
STORY_NAME = "starter"
WINDOW_SIZE = 600


def start_scene(data):
    with open(data) as fh:
        scene_data = json.load(fh)
    start_scene = scene_data.get("scenes")
    print(start_scene["start"].get("text"))
    choices= start_scene["start"]["choices"]
    print(choices)
    num =0
    for i in range(len(choices)):
        text, scene_key = choices[i].items()
        print(f"{i+1}: {text}")

def main():
    print("Infinite Adventure")
    # TODO: your code here
    start_scene("data/" + STORY_NAME + ".json")

if __name__ == "__main__":
    main()
