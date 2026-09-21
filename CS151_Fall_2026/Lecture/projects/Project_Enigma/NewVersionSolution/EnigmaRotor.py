from EnigmaConstants import ALPHABET


class EnigmaRotor:
    """
    Defines an EnigmaRotor object for use in the EnigmaMachine.
    """

    def __init__(self, wiring):
        # self._permutation = permutation_string
        # self._rev_permutation = reverse_permutation(permutation_string)
        self._wiring_offsets = wiring.copy()
        self._rev_wiring_offsets = reverse_offsets(wiring.copy())
        self._offset = 0

    def get_offset(self):
        """Gets the rotor offset

        Returns:
            (int): the current rotor offset
        """
        return self._offset

    def advance(self):
        """Advances the rotor one position

        If the rotor wraps around, True is returned to indicate that the
        advance should carry-over to the next rotor.

        Returns:
            (bool): whether a carry-over should occur
        """
        self._offset = (self._offset + 1) % 26
        self.rotate_wiring_offsets()
        if self._offset == 0:
            return True
        return False

    def right_to_left(self, index):
        """Convenience method for passing a signal from right to left (forwards)
        though the rotor.

        Args:
            index (int): the input signal index
        Returns:
            (int): the output signal index
        """
        return (index + self._wiring_offsets[index]) % 26

    def left_to_right(self, index):
        """Convenience method for passing a signal from left to right (backwards)
        though the rotor using the reversed permutation string.

        Args:
            index (int): the input signal index
        Returns:
            (int): the output signal index
        """
        return (index + self._rev_wiring_offsets[index]) % 26

    def rotate_wiring_offsets(self):
        old = self._wiring_offsets.pop(0)
        self._wiring_offsets.append(old)
        old = self._rev_wiring_offsets.pop(0)
        self._rev_wiring_offsets.append(old)

def reverse_offsets(initial_offsets):
    L = len(initial_offsets)
    rev_offsets = [0 for _ in range(L)]
    for i in range(L):
        new = (i + initial_offsets[i]) % L
        rev_offsets[new] = (L-initial_offsets[i])
    return rev_offsets

def extra(initial_offsets):
    L = len(initial_offsets)
    rev_offsets = [0] * L
    for i in range(L):
        # But if you want positive values:
        new = (i + initial_offsets[i]) % L
        rev_offsets[new] = -initial_offsets[i] % L
    return rev_offsets



def reverse_permutation(permutation):
    """Returns the inverted permutation string.

    Necessary for passing the signal backwards through the rotors.

    Args:
        permutation (str): the original, forwards permutation string
    Returns:
        (str): the inverted permutation string
    """
    rev = ""
    for letter in ALPHABET:
        rev += ALPHABET[permutation.find(letter)]
    return rev


if __name__ == "__main__":
    R = EnigmaRotor([1,2,3,4,0])
    print(R._wiring_offsets)
    print(R._rev_wiring_offsets)
    print(extra(R._wiring_offsets))
    print(extra(extra(R._wiring_offsets)))
