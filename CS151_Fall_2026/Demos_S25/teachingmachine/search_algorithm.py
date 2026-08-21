class AdvObject:
    def __init__(self, name, loc):
        self.name = name
        self.loc = loc
    def get_loc(self):
        return self.loc

class AdvLocation:
    def __init__(self, name):
        self.name = name
        self.stuff = []
    def store(self, item):
        self.stuff.append(item)
    def retrieve_top(self):
        return self.stuff.pop()

A = AdvObject("Hammer", "RA")
B = AdvObject("Torch", "RA")
RA = AdvLocation("Room A")
RA.store(A)
RA.store(B)
ANS = RA.retrieve_top().get_loc()
print(ANS)