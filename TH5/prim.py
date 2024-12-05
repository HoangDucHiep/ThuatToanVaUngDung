import heapq

def print_mst(parent, graph, V):
    print("Cạnh \tTrọng số")
    for i in range(1, V):
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")

def prim_mst(graph, V):
    parent = [-1] * V

    key = [float('inf')] * V
    key[0] = 0

    priority_queue = [(0, 0)]  

    in_mst = [False] * V

    while priority_queue:
        
        weight, u = heapq.heappop(priority_queue)
        in_mst[u] = True

        for v in range(V):
            if graph[u][v] != 0 and not in_mst[v] and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u
                heapq.heappush(priority_queue, (key[v], v))

    print_mst(parent, graph, V)


graph = [[0, 2, 0, 6, 0],
         [2, 0, 3, 8, 5],
         [0, 3, 0, 0, 7],
         [6, 8, 0, 0, 9],
         [0, 5, 7, 9, 0]]

V = len(graph)
prim_mst(graph, V)
