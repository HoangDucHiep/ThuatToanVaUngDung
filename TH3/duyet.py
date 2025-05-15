from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    print("BFS:", end=" ")
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(graph[vertex])
    print()

def dfs(graph, start):
    visited = set()
    def dfs_recursive(v):
        if v not in visited:
            print(v, end=" ")
            visited.add(v)
            for neighbor in graph[v]:
                dfs_recursive(neighbor)
    print("DFS:", end=" ")
    dfs_recursive(start)
    print()

# Example
graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
start_vertex = 2
dfs(graph, start_vertex)
bfs(graph, start_vertex)
