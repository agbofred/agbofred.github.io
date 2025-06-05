# File: AdvGame.py

"""
This module defines the AdvGame class, which records the information
necessary to play a game.
"""

###########################################################################
# Your job in this assignment is to fill in the definitions of the        #
# methods listed in this file, along with any helper methods you need.    #
# Unless you are implementing extensions, you won't need to add new       #
# public methods (i.e., methods called from other modules), but the       #
# amount of code you need to add is large enough that decomposing it      #
# into helper methods will be essential.                                  #
###########################################################################

from AdvRoom import AdvRoom, read_room
from AdvItem import AdvItem, read_item
from tokenscanner import TokenScanner

MARKER = "-----"

class AdvGame:

    def __init__(self, prefix):
        """Reads the game data from files with the specified prefix and
        stores that information in attributes.

        Args:
            prefix (str): The prefix starting each of the file names
        Returns:
            None
        """
        self._prefix = prefix

        self._Room_list = {}
        #reads all of the rooms
        with open(prefix+"Rooms.txt") as f:
            Room = read_room(f)
            while Room is not None:
                if len(self._Room_list) ==0:
                    self._Room_list["START"] = Room
                self._Room_list[Room.get_name()]= Room
                Room = read_room(f)

        self._item_list = {}
        #reads items into the dictionary
        try:
            with open(prefix + "Items.txt") as f:
                Item = read_item(f)
                while Item is not None:
                    if len(self._item_list) == 0:
                        self._item_list["START"] = Item
                    self._item_list[Item.get_name()] = Item
                    name_i = Item.get_name()
                    
        except IOError:
            pass

        self._player_items = set()
        
        #this is the player inventory
        for name_i, Item in self._item_list.items():
            location = Item.get_initial_location()
            if location != "PLAYER":
                self._Room_list[location].add_item(name_i)
            elif location == "PLAYER":
                self._player_items.add(name_i)





    def get_room(self, name):
        """Returns the AdvRoom object with the specified name.
        Args:
            name (str): the unique name of a room
        Returns:
            (AdvRoom): the corresponding AdvRoom object
        """
        return self._Room_list[name]


    def run(self):
        """Plays the adventure game stored in this object."""
        current = "START"

         
        # """addd items to the room"""
        # if self._item_list is not None:
        #     for value in self._item_list.items():
        #         current_room = self._item_list[value.get_initial_location()]
        #         current_room.add_item(value)

        while current != "EXIT":
            current_room = self._Room_list[current]

            passages = current_room.get_passages()

            if current_room.has_been_visited() == True:
                """if the room has been visited once the short description is given instead of the full one"""
                print (current_room.get_short_description())
         
            else:
                for line in current_room.get_long_description():
                    print(line)
                    
            for item in current_room.get_contents():
                print (f"There is {self._items_list[item].get_description()} here.")

            response = input("> ").strip().upper()

            scanner = TokenScanner(response)
            scanner.ignore_whitespace()
            responses = []

            while scanner.has_more_tokens():
                responses.append(scanner.next_token())


            
            

           
            if next_room is None:
                if responses[0] == "QUIT":
                    print ("Done")
                    quit()

                elif responses[0] == "HELP":
                    print (HELP_TEXT)

                elif responses[0] == "LOOK":
                    for line in current_room.get_long_description():
                        print (line)

                elif responses[0] == "TAKE":
                    if response[1] in current_room.get_contents():
                        item = responses[1]
                        current_room.remove_item(item)
                        self._player_items.add_item(item)
                        print ("taken")

                elif responses[0] == "DROP":
                    if response[1] in self._player_items:
                        item = responses[1]
                        self._player_items.discard(item)
                        current_room.add_item(item)
                        print ("dropped")

                elif responses[0] == "INVENTORY":
                    if len(self._player_items) == 0:
                        print ("You have nothing")

                    else:
                        print ("You are carrying:")
                        for item in self._player_items:
                            print (f"   {self._player_items[item].get_description()}")


                next_room = passages.get("*", None)
            else:
                next_room = passages.get(response, None)
                if next_room is None:
                    print("I don't understand that response.")
                    
                current_room.set_visited() #tracks rooms passed through
                current = next_room


# Constants

HELP_TEXT = [
    "Welcome to Adventure!",
    "Somewhere nearby is Colossal Cave, where others have found fortunes in",
    "treasure and gold, though it is rumored that some who enter are never",
    "seen again.  Magic is said to work in the cave.  I will be your eyes",
    "and hands.  Direct me with natural English commands; I don't understand",
    "all of the English language, but I do a pretty good job.",
    "",
    "It's important to remember that cave passages turn a lot, and that",
    "leaving a room to the north does not guarantee entering the next from",
    "the south, although it often works out that way.  You'd best make",
    "yourself a map as you go along.",
    "",
    "Much of my vocabulary describes places and is used to move you there.",
    "To move, try words like IN, OUT, EAST, WEST, NORTH, SOUTH, UP, or DOWN.",
    "I also know about a number of items hidden within the cave which you",
    "can TAKE or DROP.  To see what items you're carrying, say INVENTORY.",
    "To reprint the detailed description of where you are, say LOOK.  If you",
    "want to end your adventure, say QUIT."
]
