"""
File: import_movies.py

Imports movie data from movies.csv and builds a graph.
"""

import csv
from graph import LinkedDirectedGraph

def load_movies(csv_file):
    """
    Loads movies from a CSV file and returns a dictionary.
    
    Args:
        csv_file: Path to the movies.csv file
        
    Returns:
        Dictionary mapping movie_id to (title, year)
    """
    movies = {}
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            movie_id = row['id']
            title = row['title']
            year = row['year']
            movies[movie_id] = (title, year)
    return movies

def build_movie_graph(movies_dict):
    """
    Builds a graph from the movies dictionary.
    
    Args:
        movies_dict: Dictionary of movies
        
    Returns:
        LinkedDirectedGraph with movies as vertices
    """
    graph = LinkedDirectedGraph()
    
    # Add each movie as a vertex using ID to ensure uniqueness
    for movie_id, (title, year) in movies_dict.items():
        vertex_label = f"[{movie_id}] {title} ({year})"
        graph.addVertex(vertex_label)
    
    return graph

def main():
    """Main function to load and display movie data."""
    print("Loading movies from movies.csv...")
    movies = load_movies('movies.csv')
    print(f"Loaded {len(movies)} movies")
    
    # Display first 10 movies
    print("\nFirst 10 movies:")
    for i, (movie_id, (title, year)) in enumerate(movies.items()):
        if i >= 10:
            break
        print(f"{movie_id}: {title} ({year})")
    
    # Build graph
    print("\nBuilding graph...")
    graph = build_movie_graph(movies)
    print(f"Graph created with {len(graph)} vertices")
    
    # Display graph structure
    print("\n" + "="*50)
    print("GRAPH STRUCTURE")
    print("="*50)
    print(graph)
    
    # Display first 10 vertices with their edges
    print("\n" + "="*50)
    print("FIRST 10 VERTICES AND THEIR CONNECTIONS")
    print("="*50)
    count = 0
    for vertex in graph.getVertices():
        if count >= 10:
            break
        print(f"\n{vertex}:")
        edges = list(graph.incidentEdges(str(vertex)))
        if edges:
            for edge in edges:
                print(f"  -> {edge.getToVertex()}")
        else:
            print("  (no connections)")
        count += 1

if __name__ == "__main__":
    main()
