from queue import Queue

from Graphs.AdjacencyListRepresentation import create_graph


def unweighted_shortest_path(graph):
    start_node_key = next(iter(graph.vertices))
    start_node = graph.vertices.get(start_node_key)
    start_node.set_distance(0)
    q = Queue()
    q.put(start_node)
    while not q.empty():
        current_node = q.get()
        for neighbor in current_node.get_connections():
            if neighbor.get_distance() == -1:
                neighbor.set_distance(current_node.get_distance() + 1)
                neighbor.set_previous(current_node)
                q.put(neighbor)



    for vertex in graph.vertices.values():
        print(f"Move from {start_node.get_id()} to {vertex.get_id()} in {vertex.get_distance()}")




unweighted_shortest_path(create_graph())
