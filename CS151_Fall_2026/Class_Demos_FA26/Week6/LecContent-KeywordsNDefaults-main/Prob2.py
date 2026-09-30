from sandwich import print_sandwich

def make_sandwich(bread, meat, cheese, sauce =" Ginger", is_cut= False, toasted = True):
    """Makes a desired sandwich and prints it to the terminal

    Inputs:
        bread (str): The bread to use
        meat (str): The type of meat
        cheese (str): The type of cheese
        sauce (str): The sauce
        toasted (bool): If the sandwich is toasted
        is_cut (bool): If the sandwich is to be cut in half
    Outputs:
        None
    """
    print_sandwich(bread, meat, cheese, sauce, toasted, is_cut)


if __name__ == '__main__':
    make_sandwich("Sourdough", "Turkey meat", "Swiss", "Mustard")
  
    #  make_sandwich("Sourdough", "Turkey meat")
