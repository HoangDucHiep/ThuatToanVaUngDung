class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if dist[u] != float("Inf") and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        for u, v, weight in self.edges:
            if dist[u] != float("Inf") and dist[u] + weight < dist[v]:
                print("Đồ thị chứa chu trình âm")
                return

        self.print_solution(dist)

    def print_solution(self, dist):
        print("Đỉnh\tKhoảng cách từ nguồn")
        for i in range(self.V):
            print(f"{i}\t{dist[i]}")

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    g.bellman_ford(0)