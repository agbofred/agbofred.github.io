########################################
# Name:
# Indicate any collaborators or tools used to assist you including AI:
# Estimated time spent (hrs):
########################################

"""
Allows the user to specify the direction of a selection sort.
"""

def selectionSort(lyst, reverse = False):
    """Sorts the list items in ascending order if
    reverse is False; otherwise, sorts 'em in
    descending order."""
    if not reverse:
        # Sort in ascending order, counting up
        
    else:
        # Sort in descending order, counting down


def swap(lyst, x, y):
    """Exchanges the elements at positions x and y."""


def main():
    """Tests with four lists."""
    lyst = [2, 4, 3, 0, 1, 5]
    selectionSort(lyst)
    print(lyst)
    lyst = list(range(6))
    selectionSort(lyst)
    print(lyst)
    lyst = [2, 4, 3, 0, 1, 5]
    selectionSort(lyst, reverse = True)
    print(lyst)
    lyst = list(range(6))
    selectionSort(lyst, reverse = True)
    print(lyst)

if __name__ == "__main__":
    main()
