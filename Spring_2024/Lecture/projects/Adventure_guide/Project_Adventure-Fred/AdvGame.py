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

from AdvRoom import AdvRoom
from AdvRoom import read_room

class AdvGame:

    def __init__(self, prefix):
        """Reads the game data from files with the specified prefix and
        stores that information in attributes.

        Args:
            prefix (str): The prefix starting each of the file names
        Returns:
            None
        """
        self._rooms = self.read_in_rooms(prefix)
    
    def read_in_rooms(self,prefix):
        """Reads the entire AdvGame from the data file f."""
        with open(prefix + "Rooms.txt") as f:
            #return read_course(f)
            rooms = { }
            finished = False
            while not finished:
                room = read_room(f)
                if room is None:
                    finished = True
                else:
                    name = room.get_name()
                    if len(rooms) == 0:
                        rooms["START"] = room
                    rooms[name] = room
        return rooms



    def get_room(self, name):
        """Returns the AdvRoom object with the specified name.
        Args:
            name (str): the unique name of a room
        Returns:
            (AdvRoom): the corresponding AdvRoom object
        """
        return self._rooms[name]

    def run(self):
        """Plays the adventure game stored in this object."""
        current = "START"
        while current != "EXIT":
            room = self.get_room(current)
            for line in room.get_long_description():
                print(line)
            response = input("> ").strip().upper()
            passages = room.get_passages()
            next_room = passages.get(response, None)
            if next_room is None:
                next_room = passages.get("*", None)
            if next_room is None:
                print("I don't understand that response.")
            else:
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
    "I also know about a number of objects hidden within the cave which you",
    "can TAKE or DROP.  To see what objects you're carrying, say INVENTORY.",
    "To reprint the detailed description of where you are, say LOOK.  If you",
    "want to end your adventure, say QUIT."
]
