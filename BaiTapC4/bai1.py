def greedy_coloring(graph):
    n = len(graph)
    result = [-1] * n
    result[0] = 0
    available = [False] * n
    for u in range(1, n):
        for i in range(len(graph[u])):
            if graph[u][i] == 1 and result[i] != -1:
                available[result[i]] = True
        color = 0
        while color < n and available[color]:
            color += 1
        result[u] = color
        for i in range(len(graph[u])):
            if graph[u][i] == 1 and result[i] != -1:
                available[result[i]] = False
    for u in range(n):
        print(f"Đỉnh {u} được tô màu {result[u]}")
#Test
graph = [[0, 1, 0, 1, 0],
         [1, 0, 1, 1, 0],
         [0, 1, 0, 1, 1],
         [1, 1, 1, 0, 1],
         [0, 0, 1, 1, 0]]
print("Kết quả tô màu đồ thị:")
greedy_coloring(graph)
