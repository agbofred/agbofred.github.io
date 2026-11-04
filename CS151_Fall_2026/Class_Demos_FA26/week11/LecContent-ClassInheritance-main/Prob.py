
class Vehicle:
    def __init__(self, weight, terrain):
        self.weight = weight
        self.terrain = terrain

    def __repr__(self):
        return f"Vehicle({self.weight}, {self.terrain})"

class Boat(Vehicle):
    def __init__(self, weight):
        super().__init__(weight, "water")
        # self.terrain = "water"
        
    def __repr__(self):
        return f"Boat({self.weight})"


if __name__ == '__main__':
    # Starter
    car = Vehicle(5000, "roads")
    print(car)

    ## Part A
    boats = [Boat(2000), Boat(6000), Boat(300)]
    print(boats)

    ## Part B, uncomment when ready
    #c1 = Carrier(8000, 3)
    #c2 = Carrier(6000, 2)
    #print(c1)
    #print(c2)

    ## Part C, uncomment when ready
    #c2.add_plane(500)
    #print(c2) # should see the increased weight
    #c2.add_plane(500)
    #c2.add_plane(500) # should see deck full
    #print(c2) # should see a weight of 7000

