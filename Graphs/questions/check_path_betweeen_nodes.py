

from Graphs.AdjacencyListRepresentation import Graph, Vertex

def check_path_btw_vertices(graph: Graph, start, end, visited = None):
       if start not in graph.vertices.keys() or end not in graph.vertices.keys():
            return False

       start = graph.vertices[start]
       end = graph.vertices[end]
       if not visited:
           visited = set()


       visited.add(start)
       if start == end:
           return True

       for neighbour in start.get_connections():
           if neighbour not in visited:
               return check_path_btw_vertices(graph, neighbour.get_id(), end.get_id(), visited)

       return False




def num_paths_with_vertices(graph: Graph, start, end, visited):
    if start not in graph.vertices.keys() or end not in graph.vertices.keys():
        return 0

    elif start == end:
        return 1

    elif not visited:
        visited = set()

    path_count = 0
    start = graph.vertices[start]
    visited.add(start)
    for neighbour in start.get_connections():
        if neighbour not in visited:
            path_count += num_paths_with_vertices(graph, neighbour.get_id(), end, visited)
    visited.remove(start)
    return path_count













