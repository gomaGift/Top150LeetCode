from queue import Queue

from Graphs.AdjacencyListRepresentation import crete_graph, Graph, Vertex


def bfs_traversal(traverse_graph: Graph, start: Vertex):
    q = Queue()
    start_node = start
    start_node.set_distance(0)
    start_node.set_previous(None)
    q.put(start_node)
    while not q.empty():
        current_node = q.get()
        for neighbour in current_node.get_connections():
            if neighbour.get_color() == 'white':
                neighbour.set_color('gray')
                neighbour.set_previous(current_node)
                neighbour.set_distance(current_node.get_distance() + 1)
                q.put(neighbour)
            current_node.set_color("black")

        if current_node.get_previous():
            print(
                f"traversed: {current_node.get_previous().get_id()}-{current_node.get_id()}-{current_node.get_distance()}")
        else:
            print(f"traversed: None-{current_node.get_id()}-{current_node.get_distance()}")


graph = crete_graph()

def bfs(traverse_graph: Graph):
    for vertex in traverse_graph.vertices.values():
        if vertex.get_color() == 'white':
            bfs_traversal(traverse_graph,vertex)

bfs(graph)



