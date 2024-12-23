from queue import Queue

from Graphs.AdjacencyListRepresentation import crete_graph


def topological_sort(graph):
     result = [] # list for a sorted list
     no_in_degree = Queue()  # for vertices with indegree 0
     for vertex in graph.vertices.values():
         if vertex.get_in_degree() == 0:
             no_in_degree.put(vertex)

     while not no_in_degree.empty():
         vertex = no_in_degree.get()
         result.append(vertex.get_id())
         for neighbor in vertex.get_connections():
             neighbor.set_in_degree(neighbor.get_in_degree() - 1)
             if neighbor.get_in_degree() == 0:
                 no_in_degree.put(neighbor)
     if len(result) != len(graph.vertices):
         raise ValueError("The graph is not acyclic")

     return result


g = crete_graph()
print(topological_sort(g))