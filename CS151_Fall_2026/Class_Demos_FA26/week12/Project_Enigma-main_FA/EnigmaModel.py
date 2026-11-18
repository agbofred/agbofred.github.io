######################################################################
# Name:
# Who did you work with (if anyone):
# GenAI transcript (if used):
# Section leader's name:
# List of extensions made (if any):
######################################################################

""" This is the starter file for the Enigma project. """
import run_journal
from EnigmaView import EnigmaView

# You might want to import the constants here also
import EnigmaConstants as ec

class EnigmaModel:

    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = [ ]
        self._key_state = {alph: False for alph in ec.ALPHABET}
        self._lamb_state = {alph: False for alph in ec.ALPHABET}
        # Algorithm: For each letter in the alphabet, add a dictionary entry with value False.
        
        
         

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        """Function called by the view to determine if a key is currently pressed."""
        # Algorithm: Look up the given letter in _key_state, the dictionary
        # initialized in __init__. Return its value: True if the key is down,
        # or False if it is up.
        return self._key_state[letter]       # In the starter version, keys are all up

    def is_lamp_on(self, letter):
        """Function called by the view to determine if a lamp is currently lit."""
        # Algorithm: Look up the given letter in _lamb_state, the dictionary
        # initialized in __init__. Return its value: True if the lamp is on,
        # or False if it is off.
        return self._lamb_state[letter]        # In the starter version, lamps are all off

    def key_pressed(self, letter):
        """Function called by the controller whenever a key is pressed."""
        # You need to fill in this code, but leave the update call at the end
        
        # Algorithm: Use the given letter as the key in _keys_pressed and set
        # its value to True to record that the key is pressed.
        self._key_state[letter] = True
        self.update()

    def key_released(self, letter):
        """Function called by the controller whenever a key is released."""
        # You need to fill in this code, but leave the update call at the end
        
        # Algorithm: Use the released letter as the key in _keys_pressed and set
        # its value to False to record that the key is no longer pressed.
        self._key_state[letter] = False
        self.update()

    def get_rotor_letter(self, rotor_index):
        """Function called by the view to determine what letter 
        a rotor should display."""
        return "A"          # In the starter version, all rotors are set to "A"

    def rotor_clicked(self, rotor_index):
        """Function called by the controller whenever a rotor is clicked."""
        # You need to fill in this code, but leave the update call at the end
        self.update()


def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code

if __name__ == "__main__":
    enigma()
