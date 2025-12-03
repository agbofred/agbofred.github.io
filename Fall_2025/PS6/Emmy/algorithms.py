import math
from graph import LinkedStack


def topoSort(g, startLabel = None):
    stack = LinkedStack()
    g.clearVertexMarks()
    for v in g.getVertices():
        if not v.isMarked():
            dfs(g, v, stack)
    return stack
def dfs(g, v, stack):
    v.setMark()
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            dfs(g, w, stack)
    stack.push(v)

def shortestPaths(graph, startLabel):
    #returns a list containing the edges in the minimum spanning tree of the graph
    print("yuh")
    startVertex = graph.getVertex(startLabel)
    if not startVertex:
        return []
    all_vertices = list(graph.getVertices())
    n_vertices = len(all_vertices)
    label_to_index = {}
    for i, v in enumerate(all_vertices):
        label_to_index[v.label] = i
    start_index = label_to_index[startLabel]
    visited = [False] * n_vertices
    min_edge = [(math.inf, None)] * n_vertices
    min_edge[start_index] = (0, None)
    edges = []
    for k in range(n_vertices):
        min_weight = math.inf
        u_index = -1
        for j in range(n_vertices):
            if not visited[j] and min_edge[j][0] < min_weight:
                min_weight = min_edge[j][0]
                u_index = j
        if u_index == -1 or min_weight == math.inf:
            break
        visited[u_index] = True
        edge_to_add = min_edge[u_index][1]
        if edge_to_add is not None:
            edges.append(edge_to_add)
        u_vertex = all_vertices[u_index]
        for edge in u_vertex.edgeList:
            v_vertex = edge.vertex2
            v_index = label_to_index.get(v_vertex.label, -1)
            if v_index != -1 and not visited[v_index]:
                if edge.weight < min_edge[v_index][0]:
                    min_edge[v_index] = (edge.weight, edge)
    return edges



def spanTree(graph, startLabel):
    #Returns two dimensional grid of N rows and three columns where N is the number of vertices.
    #The first column contains the vertices. The second column contains the distance from the
    #start vertex to this vertex. The third column contains the immediate parent vertex of this
    #vertex, if there is one, or None otherwise.
    print("yuh")
    startVertex = graph.getVertex(startLabel)
    if not startVertex:
        return []
    label_to_index = {}
    all_vertices = list(graph.getVertices())
    for i, v in enumerate(all_vertices):
        label_to_index[v] = i
    n_vertices = len(all_vertices)
    results_grid = []
    distance = [math.inf] * n_vertices
    parent = [None] * n_vertices
    visited = [False] * n_vertices
    start_index = label_to_index[startLabel]
    distance[start_index] = 0
    for k in range(n_vertices):
        dist = math.inf
        u_index = -1
        for j in range(n_vertices):
            if not visited[j] and distance[j] < dist:
                distance[j] = dist
                u_index = j
        if u_index == -1 or dist == math.inf:
            break
        visited[u_index] = True
        u_vertex = all_vertices[u_index]
        for edge in u_vertex.edgeList:
            v_vertex = edge.vertex2
            v_index = label_to_index[v_vertex.label]
            new_dist = distance[u_index] + edge.weight
            if not visited[v_index] and new_dist < distance[v_index]:
                distance[v_index] = new_dist
                parent[v_index] = u_vertex.label
    for i in range(n_vertices):
        vertex_label = all_vertices[i].label
        dist = distance[i]
        if dist != math.inf:
            dist_display = dist
        else:
            dist_display = 'inf'
        results_grid.append([vertex_label, dist_display, parent[i]])
    return results_grid