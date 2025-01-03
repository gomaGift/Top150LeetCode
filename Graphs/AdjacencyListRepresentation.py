from sys import maxsize

class Vertex:
    def __init__(self, value):
        self.distance = maxsize
        self.id = value
        self.neighbors = {}
        self.previous = None
        self.visited = False
        self.color = "white"
        self.in_degree = 0
        self.out_degree = 0

    def set_in_degree(self, value):
        self.in_degree = value

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]

    def set_out_degree(self, value):
        self.out_degree = value

    def get_in_degree(self):
        return self.in_degree

    def get_out_degree(self):
        return self.out_degree

    def add_neighbour(self, neighbor, cost):
        self.neighbors[neighbor] = cost
    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

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


    def add_edge(self, vertex1, vertex2, cost = 1):
        if vertex1 not in self.vertices:
            self.add_vertex(vertex1)
        if vertex2 not in self.vertices:
            self.add_vertex(vertex2)

        self.vertices[vertex1].add_neighbour(self.vertices[vertex2], cost)
        self.vertices[vertex2].set_in_degree(self.vertices[vertex2].get_in_degree() + 1)
        # if undirected
        # self.vertices[vertex2].add_neighbour(self.vertices[vertex1], cost)




    def get_vertex(self, vertex_id):
        return self.vertices.get(vertex_id, None)


    def get_edges(self):
        edges = []
        for vertex in self.vertices.values():
            for neighbour, weight in vertex.neighbors.items():
                edges.append((vertex.get_id(), neighbour.get_id(), weight))

        return edges




