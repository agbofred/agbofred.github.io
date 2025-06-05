# File: AdvRoom.py

"""This module is responsible for modeling a single room in Adventure."""

#########################################################################
# Your job in this assignment is to fill in the definitions of the      #
# methods listed in this file, along with any helper methods you need.  #
# The public methods shown in this file are the ones you need for       #
# Milestone #1.  You will need to add other public methods for later    #
# milestones, as described in the handout.                              #
#########################################################################

# Constants

from AdvItem_c import AdvItem, read_item

MARKER = "-----"

class AdvRoom:

    def __init__(self, name, shortdesc, longdesc, passages):
        """Creates a new room with the specified attributes.
        
        Args:
            name (str): the unique name of the room
            shortdesc (str): a short description of the room
            longdesc (list[str]): a list of strings making up a longer description
            passages (dict[str:str]): a dictionary of possible directions and
                corresponding room names
        Returns:
            None
        """
        self._name = name
        self._shortdesc = shortdesc
        self._longdesc = longdesc
        self._passages = passages
        self._visited = False
        self._items = {}   #empty dictionary that will add the items into a room
        

    def get_name(self):
        """Returns the name of this room."""
        return self._name

    def get_short_description(self):
        """Returns the one-line short description of this room.."""
        return self._shortdesc
    def get_long_description(self):
        """Returns the list of lines describing this room."""
        return self._longdesc

    def get_passages(self):
        """Returns the dictionary mapping directions to names."""
        return self._passages

    def set_visited(self):
        """classifies the room as visited"""
        self._visited = True

    def has_been_visited(self):
        """Returns the rooms that have been visited"""
        return self._visited

    def add_item(self, item):
        self._items.add(item)
        
    def remove_item(self, item):
        if self.contains_item:
            self._items.remove(item)

    def contains_item(self, item):
        if item in self._items:
            return True
        else:
            return False

    def get_contents(self):
        return self._items.copy()
        

# Method to read a room from a file

def read_room(f):
    """Reads the next room from the file, returning None at the end.

    Args:
        f (file handle): the file handle of the text file being read
    Returns:
        (AdvRoom or None): either an AdvRoom object or None if at end of file
    """
    name = f.readline().rstrip()
    if name == "":
        return None

    shortdesc = f.readline().rstrip()

    longdesc = []
    finished = False

    while not finished:
        line = f.readline().rstrip()
        if line == MARKER:
            finished = True
        else:
            longdesc.append(line)

    """in this is where you would look for the item by calling the read_item function in a similar manner
    as the read_room function in AdvGame"""

    passages = {}
    finished = False

    while not finished:
        line = f.readline().rstrip()
        if line == "":
            finished = True

        else:
            colon = line.find(":")
            if colon == -1:
                raise ValueError("Missing colon in "+ line)
            response = line[:colon].strip().upper()
            next_question = line[colon +1:].strip()
            passages[response] = next_question
    return AdvRoom(name, shortdesc, longdesc, passages)

