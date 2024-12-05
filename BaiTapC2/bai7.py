from collections import deque


def rotOrange(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    queue = deque()        # use for BFS
    fresh_oranges = 0
    
    for r in range(rows):
        for c in range(cols):
            if (matrix[r][c] == 2):
                queue.append((r, c))   #append a tuple
            elif (matrix[r][c] == 1):
                fresh_oranges += 1
        
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] #left, right, down, up
    minutes_passed = 0
    
    while queue and fresh_oranges > 0:
        minutes_passed += 1
        
        for _ in range(len(queue)):
            cur_x, cur_y = queue.popleft()
            for d_x, d_y in directions:
                n_x = cur_x + d_x
                n_y = cur_y + d_y
                
                if (0 <= n_x < rows and 0 <= n_y < cols and matrix[n_x][n_y] == 1):
                    matrix[n_x][n_y] = 2 #rot
                    queue.append((n_x, n_y))
                    fresh_oranges -= 1
                    
    return minutes_passed if fresh_oranges == 0 else -1

if __name__ == "__main__":
    matrix1 = [
                [2, 1, 0, 2, 1],
                [1, 0, 1, 2, 1], 
                [1, 0, 0, 2, 1]
            ]
    
    matrix2 =  [ 
                [2, 1, 0, 2, 1], 
                [0, 0, 1, 2, 1], 
                [1, 0, 0, 2, 1]
            ]
    
    print("== Test 1 ==")
    print("matrix1 = ")
    for row in matrix1:
        print(row)
    print("==> Result: ", rotOrange(matrix1))
    
    print("\n== Test 2 ==")
    print("matrix2 = ")
    for row in matrix2:
        print(row)
    print("==> Result: ", rotOrange(matrix2))