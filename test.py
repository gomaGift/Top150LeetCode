from Graphs.AdjacencyListRepresentation import create_graph
from Graphs.BellmanFoldAlgorithm import bellman_ford_algorithm, bellman_ford_with_q
from Graphs.DIjkstra import dijkstra

bellman_ford_algorithm(create_graph())
bellman_ford_with_q(create_graph())