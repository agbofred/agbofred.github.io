import json

with open("data/original_big.json") as fh:
    story_data = json.load(fh)

scenes = story_data.get('scenes')

for scene_name in scenes:
    for choice in scenes[scene_name].get('choices'):
        dest = choice.get('scene_key')
        if dest not in scenes:
            print(dest)
