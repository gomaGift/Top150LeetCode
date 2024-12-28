from Graphs.questions.check_path_betweeen_nodes import num_paths_btw_src_to_dest


class Graph:
    def __init__(self, graph = {}):
        self.vertices = graph

    def get_vertices(self):
        return self.vertices.keys()

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
         self.vertices[vertex] = []

    def add_edge(self, edge):
        vertex1, vertex2 = edge
        if vertex1 not in self.vertices:
            self.vertices[vertex1] = []
        if vertex2 not in self.vertices:
            self.vertices[vertex2] = []

        self.vertices[vertex1].append(vertex2)


g = {
     "a": ["b", "c"],
     "b": ["d", "e"],
     "c" : ["d", "e"],
     "d": ["e"],
     "e": ["a"],
     "f" : []

}
G = Graph(g)
print(num_paths_btw_src_to_dest(G, 'a', 'e', None))