from collections import deque

def sum_min_max(arr, k):
    if len(arr) < k:
        return 0

    min_deque = deque()
    max_deque = deque()
    result = 0
    
    for i in range(len(arr)):
        if min_deque and min_deque[0] <= i - k:
            min_deque.popleft()
        if max_deque and max_deque[0] <= i - k:
            max_deque.popleft()
            
        while min_deque and arr[min_deque[-1]] >= arr[i]:
            min_deque.pop()
        min_deque.append(i)

        while max_deque and arr[max_deque[-1]] <= arr[i]:
            max_deque.pop()
        max_deque.append(i)

        if i >= k - 1:
            min_val = arr[min_deque[0]]
            max_val = arr[max_deque[0]]
            result += min_val + max_val
    return result

arr = [2, 5, -1, 7, -3, -1, -2]
k = 4
print(sum_min_max(arr, k)) 
