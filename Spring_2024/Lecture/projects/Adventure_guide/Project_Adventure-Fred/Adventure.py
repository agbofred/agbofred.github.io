# File: Adventure.py
# Name: your name
# Partner: partners name if applicable
# Description of any extensions:

"""This file runs the Adventure game."""

# Implementation notes
# --------------------
# The only change you need to make in this file is the definition of
# DATA_FILE_PREFIX, which should be one of the following strings:
#
#    "Tiny"      A four-room Adventure with no objects or synonyms
#    "Small"     A 12-room Adventure that tests all the features
#    "Crowther"  The full 77-room Adventure game

from AdvGame import AdvGame

# Constants

DATA_FILE_PREFIX = "/Users/fjagbo/Documents/GitHub/agbofred.github.io/Spring_2024/Lecture/projects/Adventure_guide/Project_Adventure-Fred/Tiny"

# Main program

def adventure():
    game = AdvGame(DATA_FILE_PREFIX)
    game.run()

# Startup code

if __name__ == "__main__":
    adventure()
