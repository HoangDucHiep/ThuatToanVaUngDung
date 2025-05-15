def welsh_powell_coloring(graph):
    n = len(graph)
    degree = [sum(row) for row in graph]
    sorted_vertices = sorted(range(n), key=lambda x: degree[x], reverse=True)
    result = [-1] * n
    color = 0
    for vertex in sorted_vertices:
        if result[vertex] == -1:
            result[vertex] = color
            for neighbor in sorted_vertices:
                if result[neighbor] == -1 and all(graph[neighbor][i] == 0 or result[i] != color for i in range(n)):
                    result[neighbor] = color
            color += 1
    for u in range(n):
        print(f"Đỉnh {u} được tô màu {result[u]}")
#test
graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0]
]
print("Kết quả tô màu đồ thị (Welsh-Powell):")
welsh_powell_coloring(graph)