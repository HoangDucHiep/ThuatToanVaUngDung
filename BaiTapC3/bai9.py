def flood_fill(image, sr, sc, new_color):
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]
    if original_color == new_color:
        return image
    
    def dfs(x, y):
        if x < 0 or x >= rows or y < 0 or y >= cols or image[x][y] != original_color:
            return
        image[x][y] = new_color
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        
    dfs(sr, sc)
    return image

# Ảnh mẫu
image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
sr, sc = 1, 1
new_color = 2
result = flood_fill(image, sr, sc, new_color)
print("Hình ảnh sau khi tô màu:")
for row in result:
    print(row)