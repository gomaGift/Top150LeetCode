import heapq

from Graphs.AdjacencyListRepresentation import Graph, create_graph


def dijkstra(graph: Graph):
    source_key = next(iter(graph.vertices))
    source_node = graph.vertices[source_key]
    source_node.set_distance(0)
    unvisited_nodes = [(v.get_distance(), v.get_id()) for v in graph.vertices.values()]
    heapq.heapify(unvisited_nodes)

    while len(unvisited_nodes):
        node_distance, node_id = heapq.heappop(unvisited_nodes)
        node = graph.get_vertex(node_id)
        if node.get_visited():
            continue
        node.set_visited(True)
        for neighbour in node.get_connections():
            if neighbour.get_visited():
                continue

            new_distance = node_distance + node.get_weight(neighbour)
            if new_distance < neighbour.get_distance():
                neighbour.set_distance(new_distance)
                neighbour.set_previous(node)
                print(f"update: Distance for {neighbour.get_id()} to {new_distance}")
            else:
                print(f"Not updated: Distance for {neighbour.get_id()} remained: {neighbour.get_distance()}")

        unvisited_nodes = [(v.get_distance(), v.get_id()) for v in graph.vertices.values() if not v.get_visited()]
        heapq.heapify(unvisited_nodes)






