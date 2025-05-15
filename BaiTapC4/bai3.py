import heapq

def prim(graph):
    n = len(graph)
    min_heap = [(0, 0)]
    in_mst = [False] * n
    total_weight = 0
    mst_edges = []
    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if in_mst[u]:
            continue
        in_mst[u] = True
        total_weight += weight
        if weight != 0:
            mst_edges.append((prev_u, u))
        for v, w in enumerate(graph[u]):
            if not in_mst[v] and w != 0:
                heapq.heappush(min_heap, (w, v))
                prev_u = u
    return mst_edges, total_weight
#test
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
mst_edges, total_weight = prim(graph)
print("Cây bao trùm tối thiểu:")
for edge in mst_edges:
    print(f"Cạnh: {edge}")
print(f"Tổng trọng số của cây bao trùm tối thiểu: {total_weight}")
