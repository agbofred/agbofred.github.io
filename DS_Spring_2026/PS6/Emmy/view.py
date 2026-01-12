from model import GraphDemoModel
from algorithms import shortestPaths, spanTree, topoSort

class GraphDemoView(object):
    def __init__(self):
        self.model = GraphDemoModel()
    def run(self):
        menu = "Main menu\n" + \
        "   1   Input a graph from the keyboard\n" + \
        "   2   Input a graph from a file\n" + \
        "   3   View the current graph\n" + \
        "   4   Single-source shortest paths\n" + \
        "   5   Minimum spanning tree\n" + \
        "   6   Topological sort\n" + \
        "   7   Exit the program\n"
        while True:
            command = self.getCommand(menu)
            if command == 1: self.getFromKeyboard()
            elif command == 2: self.getFromFile()
            elif command == 3:
                print(self.model.getGraph())
            elif command == 4:
                print("Paths:\n",
                      self.model.run(shortestPaths))
            elif command == 5:
                print("Tree:",
                      " ".join(map(str,
                                   self.model.run(spanTree))))
            elif command == 6:
                print("Sort:",
                      " ".join(map(str,
                                   self.model.rn(topoSort))))
            else:
                break
    def getCommand(self, menu):
        command = input(menu)
        return int(command)
    def getFromKeyboard(self):
        rep = ""
        while True:
            edge = input("Enter an edge or return to quit: ")
            if edge == "": break
            rep += edge + " "
        startLabel = input("Enter the start label: ")
        print(self.model.createGraph(rep, startLabel))
    def getFromFile(self):
        print("yup")
        #Excercise

GraphDemoView().run()