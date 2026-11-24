"""
A warmup exercise (Milestone 0) to ensure that the needed story data can be brought
into the program and navigated. DON'T FORGET TO UPLOAD THIS!
"""

import json


def print_deadends():
    """A function to open the 'original_small.json' story and print out all
    the 'dead-end' scene keys from it.
    """

    # Open up the file and read in the json data
    with open("data/starter.json") as fh:
        data = json.load(fh)
    scenes = data.get("scenes")
    # print(scenes)
    
    for game_scene in scenes:
        for choice in scenes[game_scene].get('choices'):
            dest = choice.get('scene_key')
            # print(dest)
            # print("#" * 20)
            
            if dest not in scenes:
                print(dest)

    # Loop over and navigate the data to print out the desired scene keys


if __name__ == "__main__":
    print_deadends()
