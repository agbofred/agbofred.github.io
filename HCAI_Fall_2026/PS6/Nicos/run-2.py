from graph import LinkedDirectedGraph

def add_v(g):
    label = prompt(f'Vertex Label: ')
    if label == "":
        print('Error: label cannot be blank')
        return
    
    try:
        g.addVertex(label)
        print(f'Vertex Added: ', label)


    except Exception as e:
        print('Error', e)

def add_E(g):
    from_label = prompt("From vertex: ")
    to_label = prompt(f'To vertex: ')
    weight_str = prompt(f'Weight: ')

    if from_label == "" or to_label == "":
        print(f'Error: label cannot be blank')
        return
    
    try:
        weight = float(weight_str)
    
    except ValueError:
        print(f'Error: Weight must be a number')
        return
    
    try:
        g.addEdge(from_label, to_label, weight)
        print(f'Added edge: ', from_label, "to", to_label, "with weight", weight)

    except Exception as e:
        print('Error:', e)

def display_graph(g):
    print(f'---Graph---')
    print (g)


def load_g():
    path = prompt(f'File path: ')
    if path == "":
        print(f'Error: file path cannot be blank.')
        return None
    
    g = LinkedDirectedGraph()

    try:
        f = open(path, "r")
        lines = f.readlines()
        f.close()

    except Exception as e:
        print(f'Error', e)
        return None
    
    f = open(path, "r")
    lines = f.readlines()
    f.close()

    first = lines[0].strip()
    labels = first.split(":", 1)[1].split()
    for v in labels:
        g.addVertex(v)


    line_num = 1
    for line in lines[1:]:
        line_num += 1
        parts = line.strip().split(":", 1)[1].split()
        u = parts[0]
        v = parts[1]
        w = float(parts[2])
        g.addEdge(u, v, w)

    
    print("Graph loaded.")
    return g


def short_path(g):
    if g.sizeVertices() == 0:
        print(f'Graph Empty')
        return
    
    start = prompt(f'Start Vertex')

    try:
        dist =  g.shortestPaths(start)
    except Exception as e:
        print('Error', e)
        return
    
    print(f'Shortest paths from', start + ":")

    labels = list(dist.keys())
    labels.sort()

    for label in labels:
        d = dist[label]
        if d == float('inf'):
            print(" ", start, 'to', label + ':', 'out of reach')
        else:
            print(' ', start, 'to', label + ':', d)


def mst_u(g):
    if g.sizeVertices == 0:
        print(f'Graph Empty')
        return
    
    start = prompt(f'Start vertex:')

    try:
        mst = g.minimumSpanningTree(start)
        print(f'MST (Prim) result:')
        print(mst)
    
    except Exception as e:
        print(f'Error', e)

def topo_u(g):
    if g.sizeVertices() == 0:
        print(f'Graph is empty')
        return
    
    try:
        order = g.topologicalSort()
    
    except Exception as e:
        print('Error', e)
        return
    
    if order is None:
        print(f'Graph is cyclical')

    else:
        print(f'Topological Sort:', ' '.join(order))

def alg_menu(g):
    while True:
        algomenu()
        inp = prompt(f'Put your input here: ')

        if inp == '1':
            short_path(g)
        elif inp == '2':
            mst_u(g)
        elif inp ==  '3':
            topo_u(g)
        elif inp == '4':
            return
        else:
            print(f'Please enter a number 1-4')

def prompt(msg):
    return input(msg).strip()

def menu(current_graph, saved_graph):
    print("Current graph:", current_graph.sizeVertices(), "vertices,", current_graph.sizeEdges(), "edges")

    if saved_graph is None:
        print("Saved graph: (none)")
    else:
        print("Saved graph:", saved_graph.sizeVertices(), "vertices,", saved_graph.sizeEdges(), "edges")

    print(f'1. Make a new graph')
    print(f'2. Save a graph')
    print(f'3. Load saved graph')
    print(f'4. Add a vertex')
    print(f'5. Add an edge')
    print(f'6. Display graph')
    print(f'7. Choose an algorithm')
    print(f'8. Quit')

def algomenu(g):
    print(f'\nAlgorithms!')
    print(f'1. Shortest Paths (Djikstra)')
    print(f'2. Minimum Spanning Tree (Prim)')
    print(f'3. Topological sort (Kahn)')
    print(f'4. Back')


def main():
    current_graph = LinkedDirectedGraph()
    saved_graph = None

    while True:
        menu(current_graph, saved_graph)

        inp = prompt('Put your input here: ')

        if inp == '1':
            current_graph = LinkedDirectedGraph()
            print(f'Created new graph!')

        elif inp == '2':
            saved_graph = current_graph
            print(f'Current graph saved!')
        
        elif inp == '3':
            if saved_graph == None:
                print(f'No saved graph to load')
            else:
                print(f'Loading Saved Graph')
                current_graph = saved_graph
        
        elif inp == '4':
            add_v(current_graph)

        elif inp == '5':
            add_E(current_graph)

        elif inp == '6':
            display_graph(current_graph)

        elif inp == '7':
            alg_menu(current_graph)

        elif inp == '8':
            print('Happy Graphing!')
            break

        else:
            print(f'Please enter a number 1-8')


if __name__ == "__main__":
    print(f'\nWelcome to my Graph Creator! What would you like to do?')
    main()
