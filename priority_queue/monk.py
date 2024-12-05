import heapq

class MaxHeapObj:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        # Đảo ngược so sánh để heap nhỏ trở thành heap lớn
        return self.val > other.val

def monk(i, arr):
    pq = []
    
    # Thay vì phủ định giá trị, sử dụng đối tượng MaxHeapObj
    for count in range(i):
        heapq.heappush(pq, MaxHeapObj(arr[count]))
    
    # Pop các giá trị và trả về tổng
    return heapq.heappop(pq).val + heapq.heappop(pq).val + heapq.heappop(pq).val

print(monk(4, [5, 6, 7, 9, 1, 7]))
