from queue import Queue

from Graphs.AdjacencyListRepresentation import Graph, crete_graph


def bfs(start):
    q = Queue()

    start.set_previous(None)
    start.set_distance(0)
    q.put(start)
    while not q.empty():
        curr_node = q.get()
        for neighbour in curr_node.get_connections():
            if neighbour.get_color() == "white":
                neighbour.set_distance(curr_node.get_distance() + 1)
                neighbour.set_color("gray")
                neighbour.set_previous(curr_node)
                q.put(neighbour)
            curr_node.set_color("black")
        if curr_node.get_previous():
           print(f"Traversing: {curr_node.get_id()} - {curr_node.get_previous().get_id()} - {curr_node.get_distance()}")
        else:
            print(
                    f"Traversed: None - {curr_node.get_id()} - {curr_node.get_distance()}")


def bfs_traversal(graph: Graph):

    for vertex in graph.vertices.values():
        if vertex.get_color() == 'white':
            bfs(vertex)



g = crete_graph()
bfs_traversal(g)