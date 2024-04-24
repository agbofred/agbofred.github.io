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

# Method to read a room from a file

def read_room(f):
    """Reads the next room from the file, returning None at the end.

    Args:
        f (file handle): the file handle of the text file being read
    Returns:
        (AdvRoom or None): either an AdvRoom object or None if at end of file
    """
    name = f.readline().rstrip()             # Read the question name
    if name == "":                           # Returning None at the end
        return None
    shortdesc = f.readline().rstrip()
    text = [ ]                               # Read the question text
    finished = False
    while not finished:
        line = f.readline().rstrip()
        if line == MARKER:
            finished = True
        else:
            text.append(line)

    passages = { }                            # Read the answer dictionary
    finished = False
    while not finished:
        line = f.readline().rstrip()
        if line == "":
            finished = True
        else:
            colon = line.find(":")
            if colon == -1:
                raise ValueError("Missing colon in " + line)
            response = line[:colon].strip().upper()
            next_passage = line[colon + 1:].strip()
            passages[response] = next_passage

    return AdvRoom(name, shortdesc, text, passages)  # Return the completed object
