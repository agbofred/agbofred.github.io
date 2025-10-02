# ps2.py
########################################
# Your Name:
# Indicate any collaborators or tools used to assist you including AI:
# Estimated time spent (hrs):
########################################

from node import Node

def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    probe = head
    count = 0
    while probe != None:
        count += 1
        probe = probe.next
    return count

def insert(index, newItem, head):
    """Inserts newItem at position is the linked structure
    referred to by head.  Returns a reference to the new
    structure."""
    # Your code here

def printStructure(head):
    """Prints the items in the structure referred to by head."""
    probe = head
    while probe != None:
        print(probe.data, end = " ")
        probe = probe.next
    print()
    

def main():
    """Tests modifications."""
    head = None

    head = insert(0, "1", head)
    print("1:", end = " ")
    printStructure(head)

    head = insert(1, "2", head)
    print("1 2:", end = " ")
    printStructure(head)

    head = insert(0, "0", head)
    print("0 1 2:", end = " ")
    printStructure(head)

    head = insert(3, "3", head)
    print("0 1 2 3:", end = " ")
    printStructure(head)

    head = insert(1, "9", head)
    print("0 9 1 2 3:", end = " ")
    printStructure(head)

if __name__ == "__main__": main()
