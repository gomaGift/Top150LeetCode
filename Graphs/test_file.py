from Graphs.AdjacencyListRepresentation import Graph, Vertex
from Graphs.SpanningTrees import prims_algorithm
from Graphs.questions.check_path_betweeen_nodes import check_path_btw_vertices, num_paths_with_vertices


def create_graph(vertices, edges):
    graph = Graph()
    for vertex in vertices:
        graph.add_vertex(vertex)
    for v1, v2, weight in edges:
        graph.add_edge(v1, v2, weight)
    return graph



# Define vertices and edges for each algorithm

bell_ford_ids = [""]
edges_bellman_ford = [
    ('a', 'b', -1),
    ('a', 'c', 4),
    ('b', 'c', 3),
    ('b', 'd', 2),
    ('b', 'e', 2),
    ('d', 'b', 1),
    ('e', 'd', -3),
    ('d', 'c', 5)
]

edges_bellman_ford_with_q = [
    ('a', 'b', 1),
    ('b', 'c', 2),
    ('c', 'd', 3),
    ('d', 'e', 4),
    ('e', 'a', 5)
]

prims_ids = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
edges_prims = [
    ('a', 'c', 7),
    ('a', 'd', 5),
    ('d', 'c', 9),
    ('d', 'f', 6),
    ('b', 'c', 8),
    ('f', 'e', 8),
    ('f', 'g', 11),
    ('d', 'e', 15),
    ('c', 'e', 7),
    ('e', 'g', 9),
    ('b', 'e', 5)
]



# Create graphs for each algorithm
# graph_bellman_ford = create_graph(bell_ford_ids, edges_bellman_ford)
# graph_bellman_ford_with_q = create_graph(prims_ids, edges_bellman_ford_with_q)
# graph_prims = create_graph(prims_ids, edges_prims)


# # Call algorithms with the tailored graphs
# bellman_ford_algorithm(graph_bellman_ford)
# bellman_ford_with_q(graph_bellman_ford_with_q)
# prims_algorithm(graph_prims)

path_exists_edges = [
    ('a', 'c', 7),
    ('a', 'b', 5),
    ('b', 'd', 8),
    ('b', 'e', 5),
    ('c', 'd', 8),
    ('c', 'e', 7),
    ('e', 'a', 7),
    ('d', 'e', 1)
]

graph = create_graph(['a', 'b', 'c', 'd', 'e', 'f'], path_exists_edges)
print(num_paths_with_vertices(graph, 'a', 'e', None))


# g = {
#      "a": ["b", "c"],
#      "b": ["d", "e"],
#      "c" : ["d", "e"],
#      "d": ["e"],
#      "e": ["a"],
#      "f" : []
#
# }



