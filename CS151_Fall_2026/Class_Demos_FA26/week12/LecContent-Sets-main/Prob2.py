
"""
Today's stuff is pretty open ended, without required functions.
Code in whatever way makes the most sense to you!
"""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("ArtemisII.txt") as fh:
    data = fh.read()
    
    set_data = set(data)
print(set_data)
print(len(set_data))
# if " " in set_data:
#     print("SPaces exist")
   
#if data is a super set of the  alphabet
if set(ALPHABET) <= set(data.upper()):
    print("Pangram")
else:
    print("Not Pangram")


print(set(data.upper()).difference(set(ALPHABET)))