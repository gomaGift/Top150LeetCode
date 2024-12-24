from queue import Queue

from Graphs.AdjacencyListRepresentation import Graph, create_graph


def topological_sort(graph: Graph):
    without_in_degree_nodes = Queue()
    sorted_list = []

    for node in graph.vertices.values():
        if node.get_in_degree() == 0:
            without_in_degree_nodes.put(node)


    while not without_in_degree_nodes.empty():
        current_node = without_in_degree_nodes.get()
        sorted_list.append(current_node.get_id())
        for neighbour in current_node.get_connections():
            neighbour.set_in_degree(neighbour.get_in_degree() - 1)
            if neighbour.get_in_degree() == 0:
                without_in_degree_nodes.put(neighbour)


    # raise and error if the number of nodes in the result id less than the numbr of vertices i the graph
    if len(sorted_list) != len(graph.vertices):
        raise ValueError("Graph is circular")

    return sorted_list


print(topological_sort(create_graph()))