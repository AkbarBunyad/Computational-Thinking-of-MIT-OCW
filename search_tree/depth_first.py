# recursive implementation of DFS, where I give start and end nodes beforehand

def dfs_recursive(graph, start, end, visited = None, path = None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    
    visited.add(start)  
    path.append(start)

    if start == end:
        print(path)
        return True
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs_recursive(graph, neighbor, end, visited, path):
                return True
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [], 'I': [], 'J': [], 'K': [],
    'L': [], 'M': [], 'N': [], 'O': []
}
"""
result = dfs_recursive(graph, 'A', 'C')
if not result:
    print("No path found")
"""

# recursive DFS in raw format

tree = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': []
}

def dfs_recursive_raw(graph, node, visited = None, path = None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    path.append(node)
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive_raw(graph, neighbor, visited, path)
    return path

"""
result = dfs_recursive_raw(graph, 'A')
print(result)"""

# iterative DFS for comparatively large trees: when I was visualizing the tree through python visualizer, it becomes challenging to track it with recursion. Although, time and splace complexity for both is same at O(number of nodes + number of edges) and O(number of nodes), respectively, Python's recursion depth limit could cause issues, which why iterative DFS seems more preferable.

# The idea is to first push the source node to the stack, then pop it and push its neighbors to the stack.

def dfs_iterative(graph, start, visited = None, path = None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            path.append(node)
            print(node, end = " ")
            stack.extend(reversed(graph[node]))  # the crux of this reversed part is that we explore the most recently added nodes first.
    return path





