### Đưa tất cả phần tử vào set, size của set chính là số phần tử khác nhau
def bai1(arr):
    distinct_set = set(arr)
    return len(distinct_set)

# Test
if __name__ == "__main__":
    print("=== Tets 1 ===")
    arr1 = [1, 3, 3, 2]
    print(bai1(arr1)) # 3
    
    print("=== Tets 2 ===")
    arr2 = [1, 3, 3, 2, 3, 4, 5, 5, 6]
    print(bai1(arr2)) # 6
    