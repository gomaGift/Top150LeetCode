from typing import Set

from Graphs.AdjacencyListRepresentation import Graph, Vertex, crete_graph


def dfs(visited: Set[Vertex], graph: Graph, start: Vertex) -> None:
    visited.add(start)
    print("traversed: " + start.get_id())
    for neighbour in start.neighbors.keys():
        if neighbour not in visited:
            dfs(visited, graph, neighbour)



def dfs_traversal(graph: Graph) -> None:
    visited = set()
    for vertex in graph.vertices.values():
        if vertex not in visited:
            dfs(visited, graph, vertex)




grid = crete_graph()

print()
print()

dfs_traversal(grid)
