def bfs(graph, start):
    visited = set()
    queue = [start]
    result = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)


        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)


    return result




graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Using Iterative DFS
print("BFS (Iterative):", bfs(graph, 'A'))