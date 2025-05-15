import heapq
def trap_rain_water(height_map):
    if not height_map or not height_map[0]:
        return 0
    rows, cols = len(height_map), len(height_map[0])
    visited = [[False] * cols for _ in range(rows)]
    heap = []
    for r in range(rows):
        for c in range(cols):
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                heapq.heappush(heap, (height_map[r][c], r, c))
                visited[r][c] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    water_trapped = 0
    while heap:
        height, x, y = heapq.heappop(heap)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                water_trapped += max(0, height - height_map[nx][ny])
                heapq.heappush(heap, (max(height, height_map[nx][ny]), nx, ny))
                visited[nx][ny] = True
    return water_trapped

# Địa hình mẫu
height_map = [
    [1, 4, 3, 1, 3, 2],
    [3, 2, 1, 3, 2, 4],
    [2, 3, 3, 2, 3, 1]
]
result = trap_rain_water(height_map)
print(f"Tổng thể tích nước đọng lại: {result}")