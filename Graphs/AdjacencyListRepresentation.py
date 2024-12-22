from sys import maxsize


class Vertex:
    def __init__(self, value):
        self.distance = maxsize
        self.id = value
        self.neighbors = {}
        self.previous = None
        self.visited = False

    def add_neighbour(self, neighbor, cost):
        self.neighbors[neighbor] = cost

    def get_id(self):
        return self.id

    def get_previous(self):
        return self.previous

    def get_visited(self):
        return self.visited

    def set_visited(self, visited):
        self.visited = visited

    def set_previous(self, previous):
        self.previous = previous
    def set_id(self, id):
        self.id = id

    def get_connections(self):
        return self.neighbors.keys()

    def get_distance(self):
        return self.distance

    def set_distance(self, distance):
        self.distance = distance



class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, value):
        if value not in self.vertices:
            new_vertex = Vertex(value)
            self.vertices[value] = new_vertex
            self.num_vertices += 1
            return new_vertex
        return self.vertices[value]


    def add_edge(self, vertex1, vertex2, cost):
        if vertex1 not in self.vertices:
            self.add_vertex(vertex1)
        if vertex2 not in self.vertices:
            self.add_vertex(vertex2)

        self.vertices[vertex1].add_neighbour(self.vertices[vertex2], cost)
        # if undirected
        self.vertices[vertex2].add_neighbour(self.vertices[vertex1], cost)




    def get_vertex(self, vertex):
        return self.vertices.get(vertex, None)


    def get_edges(self):
        edges = []
        for vertex in self.vertices.values():
            for neighbour, weight in vertex.neighbors.items():
                edges.append((vertex.get_id(), neighbour.get_id(), weight))

        return edges


G = Graph()
G.add_vertex('a')
G.add_vertex('b')
G.add_vertex('c')
G.add_vertex('d')
G.add_vertex('e')
G.add_edge('a', 'b', 4)
G.add_edge('a', 'c', 1)
G.add_edge('c', 'b', 2)
G.add_edge('b', 'e', 4)
G.add_edge('c', 'd', 4)
G.add_edge('d', 'e', 4)

print(G.get_edges())