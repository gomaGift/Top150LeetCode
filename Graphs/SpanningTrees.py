import heapq

from Graphs.AdjacencyListRepresentation import Graph


def prims_algorithm(graph: Graph):
    source_key = next(iter(graph.vertices))
    source_node = graph.vertices.get(source_key)
    source_node.set_distance(0)
    unvisited_nodes = [(v.get_distance(), v.get_id()) for v in graph.vertices.values()]
    heapq.heapify(unvisited_nodes)

    while len(unvisited_nodes):
        vertex_id = heapq.heappop(unvisited_nodes)[1]
        vertex = graph.get_vertex(vertex_id)
        vertex.set_visited(True)
        for neighbour in vertex.get_connections():
            if neighbour.get_visited():
                continue
            new_distance = vertex.get_weight(neighbour)
            if new_distance < neighbour.get_distance():
                neighbour.set_distance(new_distance)
                neighbour.set_previous(vertex)
                print(f"Updated: Distance of {neighbour.get_id()} changed to {new_distance}")
            else:
                print(f"Not updated: distance of {neighbour.get_id()} remains {neighbour.get_distance()}")


        unvisited_nodes = [(v.get_distance(), v.get_id()) for v in graph.vertices.values() if not v.get_visited()]
        heapq.heapify(unvisited_nodes)





