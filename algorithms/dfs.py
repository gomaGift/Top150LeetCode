def dfs(graph, start):
   visited = set()
   stack = [start]
   result = []

   while stack:
      node = stack.pop()

      if node not in visited:
         visited.add(node)
         result.append(node)

      for neighbor in graph[node]:
         if neighbor not in visited:
            stack.append(neighbor)

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
print("DFS (Iterative):", dfs(graph, 'A'))  # Output: DFS traversal order starting from 'A'

# Using Recursive DFS
