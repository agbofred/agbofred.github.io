from graph import LinkedDirectedGraph
### Much of this was either directly taken or adapted from the case study itself within Fundementals of Python
    

### Imports aren't functioning properly on my computer for some reason, so I had to put these in this file.
class Array(object):
    """Represents an array."""
 
    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self.items = list()
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self.items)
     
    def __str__(self):
        """-> The string representation of the array."""
        return str(self.items)
     
    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self.items)
     
    def __getitem__(self, index):
        """Subscript operator for access at index."""
        return self.items[index]
     
    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        self.items[index] = newItem
class Grid(object):
    """Represents a two-dimensional array."""

    def __init__(self, rows, columns, fillValue = None):
        self.data = Array(rows) # recall that we previously defined the Array class which is imported  
        for row in range (rows):
            self.data[row] = Array(columns, fillValue)
    
    def getHeight(self):
        """Returns the number of rows."""
        return len(self.data)
    
    def getWidth(self):
        "Returns the number of columns."""
        return len(self.data[0])
    
    def __getitem__(self, index):
        """Supports two-dimensional indexing
        with [row][column]."""
        return self.data[index]
    
    def __str__(self):
        """Returns a string representation of the grid."""
        result = ""
        for row in range (self.getHeight()):
            for col in range (self.getWidth()):
                result += str(self.data[row][col]) + " "
            result += "\n"
        return result
class AbstractStack(object):


    """Abstract class that implements the common 
    methods for stack collections"""
    
    # Constructor
    def __init__(self, sourceCollection=None):
        self.size = 0
        if sourceCollection:
            for i in sourceCollection:
                self.push(i)
                
    def isEmpty(self):
        """Returns True if stack is empty. Otherwise, returns False 
        """
        return len(self) == 0
    
    def __len__(self):
        """Returns the number of items in stack
        """
        return self.size
    
    def __str__(self):
        """Returns the string repsentative of S
        """
        return "{" + ", ".join(map(str,self)) +"}"
class ArrayStack(AbstractStack):



    "Array-based stack collections"
    
    # Array inital capacity
    DEFAULT_CAPACITY = 10
    
    #Constructor
    """Initializes the state of self which include any items from sourcecollector"""
    def __init__(self, sourceCollection = None):
        self.items = Array(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(self, sourceCollection)
    
    # Accessors 
    def __iter__(self):
        """Supports iteration over self. Visits items bottom to top of stack"""
        cursor =0
        while cursor < len(self):
            yield self.items[cursor]
            cursor +=1
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.items[self.size -1]
    
    # Mutator functions
    
    def add(self, item):
        self.push(item)
        
    def push(self, item):
        #resizing the array here if neccesary
        if self.size == len(self):
            temp = Array(len(self)+1)
            for i in range (self.size):
                temp[i] = self.items[i]
            self.items = temp  
        self.items[len(self)] = item
        self.size +=1
        
    def clear(self):
        self.size =0
        self.items = Array(ArrayStack.DEFAULT_CAPACITY)
        
    def pop(self):
        #Check the precondition that the stack is not empty
        if self.isEmpty():
            raise KeyError("The stack is empty") 
        oldItem = self.items[len(self)-1]
        self.size -= 1
        # resize the Array here if necessary
        temp = Array(len(self.items)-1)
        # print(f"TEMP---->{len(temp)}")
        # print(f"ITEMS---->{len(self.items)}")
        for i in range(len(temp)):
            temp[i] = self.items[i]
        self.items = temp
        return oldItem

class GraphDemoModel(object):
    """The model class for the application."""
    def __init__(self):
        self.graph = None
        self.startLabel = None
    def createGraph(self, rep, startLabel):
        """Creates a graph from rep and startLabel.
        Returns a message if the graph was successfully
        created or an error message otherwise."""
        self.graph = LinkedDirectedGraph()
        self.startLabel = startLabel
        edgeList = rep.split()
        for edge in edgeList:
            if not ">" in edge:
                # A disconnected vertex
                if not self.graph.containsVertex(edge):
                    self.graph.addVertex(edge)
                else:
                    ## Error handling in case the user inputs the same vertex twice.
                    self.graph = None
                    return "Duplicate vertex"
            else:
                # Two vertices and an edge
                bracketPos = edge.find(">")
                colonPos = edge.find(":")
                if bracketPos == -1 or colonPos == -1 or bracketPos > colonPos:
                    self.graph = None
                    return "Problem with > or :"
                fromLabel = edge[:bracketPos]
                toLabel = edge[bracketPos + 1:colonPos]
                weight = edge[colonPos + 1:]
                if weight.isdigit():
                    weight = int(weight)
                if not self.graph.containsVertex(fromLabel):
                    self.graph.addVertex(fromLabel)
                if not self.graph.containsVertex(toLabel):
                    self.graph.addVertex(toLabel)
                if self.graph.containsEdge(fromLabel, toLabel):
                    ## Error handling for duplicate edges.
                    self.graph = None
                    return "Duplicate edge"
                self.graph.addEdge(fromLabel, toLabel, weight)
        vertex = self.graph.getVertex(startLabel)
        if vertex is None:
            self.graph = None
            return "Start label not in graph"
        else:
            vertex.setMark()
            return "Graph created successfully"
    def getGraph(self):
        """Returns the string rep of the graph or None if it is unavailable"""
        if not self.graph:
            return None
        else:
            return str(self.graph)
    def run(self, algorithm):
        """Runs the given algorithm on the graph and
        returns its result, or None if the graph is
        404 Chapter 12 n Graphs
        unavailable."""
        if self.graph is None:
            return None
        else:
            return algorithm(self.graph, self.startLabel)

class GraphDemoView(object):
    def __init__(self):
        self.model = GraphDemoModel()
    def run(self):
        """Menu-driven command loop for the app."""
        menu = "Main menu\n" + \
        " 1 Input a graph from the keyboard\n" + \
        " 2 Input a graph from a file\n" + \
        " 3 View the current graph\n" \
        " 4 Single-source shortest paths\n" \
        " 5 Minimum spanning tree\n" \
        " 6 Topological sort\n" \
        " 7 Exit the program\n"
        while True:
            command = self.getCommand(7, menu)
            def shortestPaths(graph, startLabel):
                # Dijkstra's algorithm is being used here.
                rows = len(graph.vertices)
                grid = Grid(rows, 3, 0)
                source_vertex = graph.getVertex(startLabel)
                i = 0
                included = [0]*rows
                for vertex in graph.vertices:
                    grid[i][0] = vertex
                    source_vertex_near = False
                    for edge in source_vertex.edgeList:
                        if edge.vertex1 == source_vertex or edge.vertex2 == source_vertex:
                            source_vertex_near = True
                            edge_weight = edge.weight
                    if vertex == startLabel:
                        grid[i][1] = 0
                        grid[i][2] = None
                        included[i] = True
                    elif source_vertex_near == True:
                        grid[i][1] = edge_weight
                        grid[i][2] = startLabel
                        included[i] = False
                    else:
                        grid[i][1] = "infinity"
                        grid[i][2] = None
                        included[i] = False
                    i += 1
                def allVertexIncluded(included):
                    ## Automated check if the task is finished or not.
                    for x in included:
                        if x == False:
                            return False
                    return True
                while not allVertexIncluded(included):
                    i = 0
                    x = 0
                    ## Set default distance and vertex
                    while x < len(included):
                        if included[x] == False:
                            lowest_distance = grid[x][1]
                            lowest_vertex = grid[x][0]
                            lowest_vertex_num = x
                        x += 1
                    while i < rows:
                        ## Iterate until the lowest distance is found
                        if not included[i]:
                            if type(grid[i][1]) == int:
                                if grid[i][1] < lowest_distance:
                                    lowest_distance = grid[i][1]
                                    lowest_vertex = grid[i][0]
                                    lowest_vertex_num = i
                                
                        i += 1
                    included[lowest_vertex_num] = True
                    i = 0
                    while i < rows:
                        ## print('figuring out T')
                        if not included[i]:
                            target_vertex = graph.getVertex(grid[i][0])
                            for edge in target_vertex.edgeList:
                               if edge.vertex2 == target_vertex:
                                   new_distance = lowest_distance + edge.weight
                                   if new_distance < grid[i][1]:
                                       grid[i][1] = new_distance
                                       grid[i][2] = lowest_vertex
                        i += 1
                return grid.__str__()            

            def spanTree(graph, startLabel):
               ## Creates a minimum spanning tree for the graph.
               unvisited = []
               for vertex in graph.vertices:
                   v = graph.vertices[vertex]
                   unvisited.append(v)
                   for edge in v.edgeList:
                       unvisited.append(edge)
               visited = []
               visited.append(unvisited[0])
               del unvisited[0]
               for vertex in graph.vertices:
                   v = graph.vertices[vertex]
                   ## "Lowest_edge" is the lowest weight edge
                   lowest_edge = None
                   for edge in v.edgeList:
                        if lowest_edge == None or edge.weight > lowest_edge.weight:
                            lowest_edge = edge
                        visited.append(lowest_edge)
                        if lowest_edge in unvisited:
                            unvisited.remove(lowest_edge)
                        visited.append(lowest_edge.vertex2)
                        if lowest_edge.vertex2 in unvisited:
                            unvisited.remove(lowest_edge.vertex2)
                        
               return visited
            def topoSort(graph, startLabel):
                ## Sorts the graph topologically,.
                unvisited = []
                visited = []
                def dfs(graph, v, stack):
                    visited.append(v)
                    if v in unvisited:
                        unvisited.remove(v)
                    proper_vertex = graph.getVertex(v)
                    for edge in proper_vertex.edgeList:
                        w = edge.vertex2.label
                        if w in unvisited:
                            dfs(graph, w, stack)

                    stack.push(v)
                unvisited.append(startLabel)
                for vertex in graph.vertices:
                    if vertex not in unvisited:
                        unvisited.append(vertex)
                stack = ArrayStack()
                for v in graph.vertices:
                    if v in unvisited:
                        dfs(graph, v, stack)
                return stack

            if command == 1: self.getFromKeyboard()
            elif command == 2: self.getFromFile()
            elif command == 3:
                print(self.model.getGraph())
            elif command == 4:
                print("Paths:\n",
                self.model.run(shortestPaths))
            elif command == 5:
                print("Tree:", " ".join(map(str,self.model.run(spanTree))))
            elif command == 6:
                print("Sort:"," ".join(map(str,self.model.run(topoSort))))
            else: break
 
    def getCommand(self, high, menu):
        """Obtains and returns a command number."""
        prompt = "Enter a number [1-" + str(high) + "]: "
        commandRange = list(map(str, range(1, high + 1)))
        error = "Error, number must be 1 to " + str(high)
        while True:
            print(menu)
            command = input(prompt)
            if command in commandRange:
                return int(command)
            else:
                print(error)
    def getFromKeyboard(self):
        """Inputs a description of the graph from the keyboard and creates the graph."""
        rep = ""
        while True:
            edge = input("Enter an edge or return to quit: ")
            if edge == "": break
            rep += edge + " "
        startLabel = input("Enter the start label: ")
        print(self.model.createGraph(rep, startLabel))
    def getFromFile(self):
        ## File must be formatted as the start label on the first line, and the second line must be the vertices and edges.
        ## For reasons I'm not quite sure of, my Visual Studio Code is refusing to read anything from files not already in the starter code.
        ## This has been an issue on previous assignments as well. For this reason, I do not know whether this functions on other computers, but it does not function on mine.
        ## The test .txt file has been included, but this algorithm cannot pull anything but blank spaces from it.

        filename = input("Enter the filename. ")
        with open(filename, "r") as filetext:
            line = filetext.readline()
            startLabel = line.strip()
            print(startLabel)
            line = filetext.readline()
            rep = line.strip()
            print(rep)
        print(self.model.createGraph(rep, startLabel))
        

GraphDemoView().run()
