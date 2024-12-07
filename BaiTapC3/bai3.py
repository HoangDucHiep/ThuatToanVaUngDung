def custom_sort_by_weight(arr, k):
    weights = [(x, x % k) for x in arr]
    sorted_weights = sorted(weights, key=lambda x: (-x[1], x[0]))
    sorted_array = [x[0] for x in sorted_weights]
    return sorted_array
A = [10, 20, 30, 40, 50, 60]
K = 7

result = custom_sort_by_weight(A, K)
print("Mảng sau khi sắp xếp:", result)

""" 
def sort_by_special_weight(A, K):
    # Tạo mảng để lưu trữ số lượng xuất hiện của từng trọng số
    count = [[] for _ in range(K)]
    
    # Tính toán trọng số đặc biệt và phân loại
    for i, num in enumerate(A):
        special_weight = num % K
        count[special_weight].append(num)
    
    # Sắp xếp các nhóm có cùng trọng số theo giá trị giảm dần
    for i in range(K):
        count[i].sort(reverse=True)
    
    # Tạo mảng kết quả
    result = []
    
    # Lấy các phần tử từ trọng số cao nhất đến thấp nhất
    for weight in range(K-1, -1, -1):
        result.extend(count[weight])
    
    return result

# Hàm kiểm tra
def main():
    # Ví dụ minh họa
    A = [10, 20, 30, 40, 50, 60]
    K = 7
    
    print("Mảng ban đầu:", A)
    sorted_array = sort_by_special_weight(A, K)
    print("Mảng sau khi sắp xếp:", sorted_array)

# Chạy hàm kiểm tra
if __name__ == "__main__":
    main()
 """