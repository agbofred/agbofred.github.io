# File: EnigmaModel.py

""" This is the starter file for the Enigma project. """

from EnigmaView import EnigmaView
import EnigmaConstants as EC
from EnigmaRotor import EnigmaRotor

class EnigmaModel:

    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = [ ]
        self._keys_pressed = {alph:False for alph in EC.ALPHABET}
        self._lamp_states = {alph:False for alph in EC.ALPHABET}
        self._rotors = [EnigmaRotor(p) for p in EC.ROTOR_WIRING]

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        """Checks if a particular key is down

        Args:
            letter (str): the letter of the key to check
        Returns:
            (bool): true if the key is down
        """
        return self._keys_pressed[letter]

    def is_lamp_on(self, letter):
        """Checks if a particular lamp is on

        Args:
            letter (str): the letter of the lamp to check
        Returns:
            (bool): true if the lamp is on
        """
        return self._lamp_states[letter]

    def key_pressed(self, letter):
        """Called whenever a key is pressed

        Handles updating the rotors, keys, and lamp states.

        Args:
            letter (str): the letter of the key that was pressed
        Returns:
            None
        """
        if self._rotors[-1].advance():
            if self._rotors[-2].advance():
                self._rotors[-3].advance()
        self._keys_pressed[letter] = True
        self._lamp_states[self._chain_signal(letter)] = True
        self.update()

    def key_released(self, letter):
        """Called whenever a key is released.

        Updates the state of the keys and lamps.

        Args:
            letter (str): the letter of the key that was released
        Returns:
            None
        """
        self._keys_pressed[letter] = False
        self._lamp_states[self._chain_signal(letter)] = False
        self.update()

    def _chain_signal(self, letter):
        """Passes a signal through the entire Enigma machine

        Args:
            letter (str): the letter corresponding to the start of the chain
        Returns:
            (str): the resulting encrypted or decrypted letter
        """
        index = EC.ALPHABET.find(letter)
        for rotor in self._rotors[::-1]: #forwards through the rotors
            index = rotor.right_to_left(index)
        index = (index + EC.REFLECTOR_WIRING[index]) % 26 #reflector
        for rotor in self._rotors: #backwards through the rotors
            index = rotor.left_to_right(index)
        letter = EC.ALPHABET[index]
        return letter

    def get_rotor_letter(self, index):
        """Gets the letter corresponding to a given rotor's current offset

        Args:
            index (int): the index of the rotor to query (0 for slow, 2 for fast)
        Returns:
            (str): the letter corresponding to the desired rotor's offset
        """
        rotor = self._rotors[index]
        return EC.ALPHABET[rotor.get_offset()]

    def rotor_clicked(self, index):
        """Handles advancing a rotor when directly clicked

        Args:
            index (int): the index of the rotor clicked (0 for slow, 2 for fast)
        Returns:
            None
        """
        rotor = self._rotors[index]
        rotor.advance()
        self.update()

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code

if __name__ == "__main__":
    enigma()
