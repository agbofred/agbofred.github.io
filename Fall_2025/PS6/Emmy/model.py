from graph import LinkedDirectedGraph

class GraphDemoModel(object):
    def __init__(self):
        self.graph = None
        self.startLabel = None
    def createGraph(self, rep, startLabel):
        self.graph = LinkedDirectedGraph()
        self.startLabel = startLabel
        edgeList = rep.split()
        for edge in edgeList:
            if not '>' in edge:
                if not self.graph.containsVertex(edge):
                    self.graph.addVertex(edge)
                else:
                    self.graph = None
                    return "Duplicate vertex"
            else:
                bracketPos = edge.find('>')
                colonPos = edge.find(';')
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
                if self.graph.containsEdge(fromLabel,toLabel):
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
        if not self.graph:
            return None
        else:
            return str(self._graph)
    def run(self, algorithm):
        if self.graph is None:
            return None
        else:
            return algorithm(self.graph, self.startLabel)