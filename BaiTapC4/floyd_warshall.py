INF = float('inf')

def floyd_warshall(graph):
    V = len(graph)
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    for i in range(V):
        if dist[i][i] < 0:
            print("\nĐồ thị chứa chu trình âm")
            return
    print_solution(dist)

def print_solution(dist):
    V = len(dist)
    print("\nKhoảng cách ngắn nhất giữa các cặp đỉnh:")
    header = "\t".join([f"Tới {j}" for j in range(V)])
    print(f"\t{header}")
    for i in range(V):
        row = []
        for j in range(V):
            if dist[i][j] == INF:
                row.append("INF")
            else:
                row.append(str(dist[i][j]))
        print(f"Từ {i}\t" + "\t".join(row))

if __name__ == "__main__":
    graph = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]
    floyd_warshall(graph)