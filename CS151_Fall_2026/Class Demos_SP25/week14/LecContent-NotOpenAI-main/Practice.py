from notopenai import NotOpenAI
import json
CLIENT = NotOpenAI(api_key="bU1AoiUR2KPqKiV9BE1d")

def lookup():
    """Uses the NotOpenAI API to look up the 5 most influential adventure games
    and saves the returned JSON data to disk.
    """
    chat_completion = CLIENT.chat.completions.create(
    messages =[
        {
            "role": "user",
            "content": " lookup and obtain a JSON structure that contains information on the top 5 most influential adventure games of all time. Your structure should include: Game name, The creator, The publishing year, A one sentence description of why it was influential"
        }
    ],
    model= "gpt-4o-mini",
    response_format={"type": "json_object"}
    )

    response_str = chat_completion.choices[0].message.content

    print(response_str)

    new_data = json.loads(response_str)

    print("X"* 100)

    print(new_data)

    with open("five_adventure_games", 'w') as fh:
        json.dump(new_data, fh, indent=2)

def process_json(filename):
    """Reads in a JSON file to print to the screen all the contained adventure
    games which are graphical in nature.
    """
    with open(filename, "r") as fh:
        data = json.load(fh)

    # The API may return either a list of games or an object containing the list.
    # games = data if isinstance(data, list) else data.get("games", [])
    # visual_clues = ("graphical", "graphics", "visual", "point-and-click")

    # for game in games:
    #     description = next(
    #         (value for key, value in game.items() if "description" in key.lower()),
    #         "",
    #     )
    #     if any(clue in str(description).lower() for clue in visual_clues):
    #         name = next(
    #             (value for key, value in game.items() if "name" in key.lower()),
    #             "Unknown game",
    #         )
    #         print(name)
    
    visual = ["graphical", "graphics", "visual", "point-and-click"]
    for game in data['top_adventure_games']:
        if game['description'] in visual:
            print(game)
        else:
            print("No graphical game")
 

    


if __name__ == '__main__':
    # lookup()
    
    # Uncomment the below line AND COMMENT THE ABOVE lookup() when ready
    # If you don't comment the above, you'll regenerate the file and 
    # the structure may change

    process_json("five_adventure_games") 
