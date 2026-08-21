class Demo:
    def __init__(self):
        self.x = []

    def add(self, v):
        self.x.append(v)

    def get_x(self):
        return self.x

A, B = Demo(), Demo()
C = B.get_x()
A.add(3)
B.add(3)
C.append(A)
#print(A.get_x() == B.get_x())
print(B.get_x())