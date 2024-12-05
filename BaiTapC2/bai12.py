import heapq

def sliding_window_max(arr, k):
    result = []
    
    window = [(-arr[i], i) for i in range(k)]
    heapq.heapify(window)
    
    result.append(-window[0][0])
    
    for i in range(k, len(arr)):
        heapq.heappush(window, (-arr[i], i))
        while window[0][1] <= i - k:
            heapq.heappop(window)
        
        result.append(-window[0][0])
    
    return result

arr = [1, 2, 3, 6, 4, 5, 2, 3, 6]
k = 3
print(sliding_window_max(arr, k))