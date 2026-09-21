import json
from notopenai import NotOpenAI
import os
from pgl import GWindow, GImage, GRect
from rich import print
from rich.console import Console

# follow the instructions in the notopenai handout to get your free api key
CLIENT = NotOpenAI(api_key="pNenSzkwFKprwfRzoCTv")
STORY_NAME = "original_small"
CONSOLE = Console()

def load_story():
    """Loads in the story provided by the given constant"""
    with open("data/" + STORY_NAME + '.json') as fh:
        story_data = json.load(fh)
    return story_data

def print_scene(scene_dict):
    """Prints one scene description and the corresponding choices"""
    # Printing description
    print(scene_dict['text'])
    # Printing choices
    for i, choice in enumerate(scene_dict['choices']):
        s = f"  {i+1}. {choice['text']}"
        print(s)

def get_valid_choice(scene_dict):
    """Prompts the user to enter a choice from the multiple options just printed

    TODO: an empty prompt should terminate the program
    """
    choice_valid = False
    num_choices = len(scene_dict['choices'])
    while not choice_valid:
        choice = input("What do you choose? ")
        if choice.isdigit() and int(choice) in range(1, num_choices+1):
            choice_valid = True
        elif choice == "":
            return None
    return int(choice)

def generate_new_scene(scene_key, story_dict, arriving_path_desc, old_key):
    """Generates a new scene when a missing scene_key in encountered

    I added the prompt by which they are entering the scene, and think it helps.
    """
    # print("\n...Suspenseful music plays as the story continues...\n")

    prompt = f"""
    Return the next scene of a story for key {scene_key}. An example scene should be formatted in json like this: {str(story_dict['scenes']['start'])}. The main plot line of the story is: {story_dict['plot']}. A user is entering this scene by {arriving_path_desc} from a scene with key {old_key}, so one choice should take them back to that scene.
    """
    with CONSOLE.status("[green]Suspenseful music plays as the story continues...[/green]"):
        chat_resp = CLIENT.chat.completions.create(
            messages=[{
                "role": "user",
                "content": prompt
            }],
            model = "gpt-4o-mini",
            response_format = {"type": "json_object"}
        )
        response_str = chat_resp.choices[0].message.content
    return json.loads(response_str)

def visualize_scene(gw, scene_key):
    """Draws a given scene to the canvas, if it exists"""
    path = f"img/{scene_key}.jpg"
    gw.clear()
    if os.path.exists(path):
        img = GImage(path)
        gw.add(img)
    else:
        rect = GRect(0,0,600,600)
        rect.set_filled(True)
        gw.add(rect)
    



def main():
    print("Infinite Story")
    story = load_story()
    gw = GWindow(600, 600)
    # canvas = Canvas(1024, 1024, 'Infinite Story')
    scenes = story['scenes']

    current_scene = 'start'
    finished = False
    while not finished:
        scene = scenes.get(current_scene)
        if not scene:
            scene = generate_new_scene(current_scene, story, path_desc, prev_scene)
            scenes[current_scene] = scene
        print()
        print_scene(scene)
        visualize_scene(gw, current_scene)
        new_scene_id = get_valid_choice(scene)
        if not new_scene_id:
            finished = True
            gw.close()
            print('Goodbye!')
        else:
            path_desc = scene['choices'][new_scene_id-1]['text']
            prev_scene = current_scene
            current_scene = scene['choices'][new_scene_id-1]['scene_key']




if __name__ == "__main__":
    main()
