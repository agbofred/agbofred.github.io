"""
File: testdirected.py

Project 12.8

Tests making a distance matrix.
"""

from graph import LinkedDirectedGraph
import random
from arrays import Array

# Define a function to print a labeled distance matrix
def printDistanceMatrix(matrix, table):
    """Prints the distance matrix with rows and columns
    labels with the index positions and vertex labels."""
    labels = Array(len(table))
    index = 0
    labelWidth = 0
    indexWidth = 0
    for label in table:
        labels[table[label]] = label
        labelWidth = max(labelWidth, len(str(label)))
        indexWidth = max(indexWidth, len(str(index)))
        index += 1

    weightWidth = 0
    for row in range(matrix.getHeight()):
        for column in range(matrix.getWidth()):
            weightWidth = max(weightWidth, len(str(matrix[row][column])))

    weightWidth = max(weightWidth, labelWidth, indexWidth)
    topRowLeftMargin = " " * (indexWidth + labelWidth + 3)
    print(topRowLeftMargin, end = "")
    for label in labels:
        print(centerJustify(label, weightWidth), end = " ")
    print()
    print(topRowLeftMargin, end = "")
    for position in range(len(labels)):
        print(centerJustify(position, weightWidth), end = " ")
    print("\n")
    for row in range(matrix.getHeight()):
        print(rightJustify(row, indexWidth),
              rightJustify(labels[row], labelWidth), end = "  ")
        for column in range(matrix.getWidth()):
            print(centerJustify(matrix[row][column], weightWidth), end = " ")
        print()

def rightJustify(data, fieldWidth):
    """Right-justifies data within the given field width."""
    data = str(data)
    numSpaces = fieldWidth - len(data)
    if numSpaces <= 0:
        return data
    else:
        return " " * numSpaces + data

def centerJustify(data, fieldWidth):
    """Centers data within the given field width."""
    data = str(data)
    numSpaces = fieldWidth - len(data)
    if numSpaces <= 1:
        return data
    else:
        spacesLeft = numSpaces // 2
        spacesRight = numSpaces // 2
        if numSpaces % 2 == 1:
            spacesLeft += 1
    return spacesLeft * " " + data + spacesRight * " "
    

# Create and print a randomly ordered list of labels
lyst = ['a','b','c','d','e','f','g']
random.shuffle(lyst)
print("The list of labels:")
print(lyst)

# Create and print a graph with those vertex labels
graph = LinkedDirectedGraph(lyst)
print("\nThe graph:")
print(graph)

# Create and print the label table for the graph
table = graph.makeLabelTable()
print("\nThe label table:")
keys = list(table.keys())
keys.sort()
for key in keys:
    print(table[key], key)

# Add some edges with weights
graph.addEdge('a', 'b', 80)
graph.addEdge('b', 'c', 79)
graph.addEdge('b', 'e', 153)
graph.addEdge('c', 'd', 78)
graph.addEdge('c', 'f', 74)
graph.addEdge('d', 'f', 89)
graph.addEdge('d', 'e', 98)
graph.addEdge('f', 'g', 67)

# Create and print the distance matrix for the graph
matrix = graph.makeDistanceMatrix(table)
print("\nThe distance matrix:")
print(matrix)

# Pretty print the labeled matrix
print("\nThe labeled distance matrix:")
printDistanceMatrix(matrix, table)

