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
import EnigmaConstants as ec 

class EnigmaModel:

    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = [ ]
        self._keys_pressed = {alph: False for alph in ec.ALPHABET}
        self._lamb_state = {alph: False for alph in ec.ALPHABET}

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        """Function called by the view to determine if a key is currently pressed."""
        
        return self._keys_pressed[letter]        # In the starter version, keys are all up

    def is_lamp_on(self, letter):
        """Function called by the view to determine if a lamp is currently lit."""
        return self._keys_pressed[letter]         # In the starter version, lamps are all off

    def key_pressed(self, letter):
        """Function called by the controller whenever a key is pressed."""
        # You need to fill in this code, but leave the update call at the end
        self._keys_pressed[letter] = True
        self.update()

    def key_released(self, letter):
        """Function called by the controller whenever a key is released."""
        # You need to fill in this code, but leave the update call at the end
        self._keys_pressed[letter] = False
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
