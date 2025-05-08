# recursive implementation of DFS, where I gave start and end nodes beforehand

def dfs(graph, start, end, visited = None, path = None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    
    visited.add(start)  
    path+=[start]

    if start == end:
        print(path)
        return True
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, end, visited, path):
                return True
    path.pop()
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['A']
}

result = dfs(graph, 'A', 'C')
if not result:
    print("No path found")