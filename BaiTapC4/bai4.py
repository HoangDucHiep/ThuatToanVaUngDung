class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    
    dsu = DisjointSet(n)
    
    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if dsu.find(u) != dsu.find(v):
            mst.append((u, v, weight))
            total_weight += weight
            dsu.union(u, v)
    
    return mst, total_weight

edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9)
]
n = 5
mst, total_weight = kruskal(n, edges)
print("Cây bao trùm tối thiểu:")
for edge in mst:
    print(f"Cạnh: {edge[0]} - {edge[1]} với trọng số: {edge[2]}")
print(f"Tổng trọng số của cây bao trùm tối thiểu: {total_weight}")
