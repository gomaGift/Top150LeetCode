class Vertex:
    def __init__(self, value):
        self.value = value
        self.visited = False

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_visited(self):
        return self.visited

    def set_visited(self, value):
        self.visited = value

    def get_connections(self):
        pass

    def add_neighbor(self, neighbor):
        pass




class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = []
        self.adjacency_matrix = [[-1] * self.num_vertices for _ in range(self.num_vertices)]
        for i in range(self.num_vertices):
            self.vertices.append(Vertex(i))


    def get_vertex(self, index):
        for i in range(len(self.vertices)):
            if index == self.vertices[i].get_value():
                return i
        else:
            return -1


    def set_vertex(self, index, value):
        if 0 <= index < self.num_vertices:
            self.vertices[index].set_value(value)

    def add_edge(self,vertex_id, neighbor_id, cost = 0):
        if self.get_vertex(vertex_id) != -1 and self.get_vertex(neighbor_id) != -1:
            self.adjacency_matrix[self.get_vertex(vertex_id)][self.get_vertex(neighbor_id)] = cost

    #         don't do this for a directed graph
            self.adjacency_matrix[self.get_vertex(neighbor_id)][self.get_vertex(vertex_id)] = cost


    def print_matrix(self):
        for i in range(self.num_vertices):
            row = []
            for j in range(self.num_vertices):
                row.append(self.adjacency_matrix[i][j])
            print(row)


    def get_edges(self):
        edges = []
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.adjacency_matrix[i][j] != -1:
                    edges.append((i, j, self.adjacency_matrix[i][j]))
        return edges

G = Graph(5)
G.set_vertex(0, 'a')
G.set_vertex(1, 'b')
G.set_vertex(2, 'c')
G.set_vertex(3, 'd')
G.set_vertex(4, 'e')

G.print_matrix()
G.add_edge('a', 'e', 10)
G.add_edge('a', 'c', 20)
G.add_edge('c', 'b', 30)
G.add_edge('b', 'e', 40)
G.add_edge('e', 'd', 50)
G.add_edge('f', 'e', 60)
print()
G.print_matrix()

print(G.get_edges())





