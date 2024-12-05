def greedy_coloring(graph, V):
    result = [-1] * V 
    result[0] = 0

    available_color = [False] * V

    for u in range(1, V):
        for i in range(V):
            if graph[u][i] == 1 and result[i] != -1:
                available_color[result[i]] = True

        color = 0
        while color < V:
            if not available_color[color]:
                break
            color += 1

        result[u] = color

        for i in range(V):
            if graph[u][i] == 1 and result[i] != -1:
                available_color[result[i]] = False

    
    for u in range(V):
        print(f"Vertex: {u} ---> Color: {result[u]}")


graph = [[0, 1, 0, 1, 0],
         [1, 0, 1, 1, 0],
         [0, 1, 0, 1, 1],
         [1, 1, 1, 0, 1],
         [0, 0, 1, 1, 0]]

V = len(graph)
greedy_coloring(graph, V)
