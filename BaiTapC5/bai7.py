def num_similar_groups(A):
    # Hàm kiểm tra tính tương tự giữa hai chuỗi
    def are_similar(s1, s2):
        diff = [(c1, c2) for c1, c2 in zip(s1, s2) if c1 != c2]
        return len(diff) == 2 and diff[0] == diff[1][::-1]

    # DFS để tìm các nhóm liên thông
    def dfs(node, visited, graph):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, visited, graph)

    n = len(A)
    graph = {i: [] for i in range(n)}

    # Xây dựng đồ thị
    for i in range(n):
        for j in range(i + 1, n):
            if are_similar(A[i], A[j]):
                graph[i].append(j)
                graph[j].append(i)

    # Đếm số thành phần liên thông
    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, graph)
            count += 1

    return count


# Test cases
test_cases = [
    (["abc", "acb", "bac", "bca", "cab", "cba"], 1),
    (["abc", "def", "ghi"], 3),
    (["singleton"], 1),
    (["abc", "acb", "xyz", "yxz", "zxy"], 2),
    (["abcd", "abdc", "bacd", "badc", "abcd", "abdc"], 1),  # Chuỗi trùng lặp
]

# Kiểm tra các test case
for i, (A, expected) in enumerate(test_cases, 1):
    result = num_similar_groups(A)
    print(f"Test case {i}: Kết quả = {result}, Kỳ vọng = {expected}, {'Đúng' if result == expected else 'Sai'}")
