from depth_first import graph

from collections import deque
def bfs(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            print(node, end=' ')
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited
bfs(graph, 'A')
print()

# The same complexity as DFS; O(V+E) as time, O(V) as space one, where V is the number of vertices or nodes, and E is the number of edges.
