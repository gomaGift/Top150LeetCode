from queue import Queue
from sys import maxsize
from Graphs.AdjacencyListRepresentation import Graph
from Graphs.DIjkstra import dijkstra

def bellman_ford_algorithm(graph: Graph):
    destination = {}
    predecessor = {}

    # Initialize distances and predecessors
    for v in graph.vertices.values():
        destination[v] = maxsize
        predecessor[v] = None

    source_key = next(iter(graph.vertices))
    source_node = graph.vertices[source_key]
    destination[source_node] = 0

    # Relax edges |V| - 1 times
    for i in range(len(graph.vertices) - 1):
        for vertex in graph.vertices.values():
            for neighbour in vertex.get_connections():
                v_neighbour_weight = destination[vertex] + vertex.get_weight(neighbour)
                if destination[neighbour] > v_neighbour_weight:
                    destination[neighbour] = v_neighbour_weight
                    predecessor[neighbour] = vertex

    # Check for negative weight cycles
    for v in graph.vertices.values():
        for neighbour in v.get_connections():
            assert destination[neighbour] <= destination[v] + v.get_weight(neighbour)

    # Print shortest distances and paths
    print("Vertex\tDistance\tPredecessor")
    for v in graph.vertices.values():
        pred = predecessor[v].get_id() if predecessor[v] else "None"
        print(f"{v.get_id()}\t{destination[v]}\t\t{pred}")


def bellman_ford_with_q(graph: Graph):
    first_key = next(iter(graph.vertices))
    source_node = graph.vertices[first_key]
    source_node.set_distance(0)
    q = Queue()
    q.put(source_node)
    source_node.set_visited(True)
    while not q.empty():
        vertex = q.get()
        vertex.set_visited(False)
        for neighbour in vertex.get_connections():
            nv_distance = vertex.get_distance() + vertex.get_weight(neighbour)
            if nv_distance < neighbour.get_distance():
                if not neighbour.get_visited():
                    q.put(neighbour)
                    neighbour.set_visited(True)
                neighbour.set_distance(nv_distance)
                neighbour.set_previous(vertex)

    print("Vertex\tDistance\tPredecessor")
    for v in graph.vertices.values():
        pred = v.get_previous().get_id() if v.get_previous() else "None"
        print(f"{v.get_id()}\t\t\t{v.get_distance()}\t\t\t{pred}")
