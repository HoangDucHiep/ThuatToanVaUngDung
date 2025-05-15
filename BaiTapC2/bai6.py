from collections import deque

def firstNegativeInWindow(arr, k):
    dq = deque()
    n = len(arr)
    results = []
    
    for i in range(n):
        #remove the element that are out of current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()
            
        if arr[i] < 0:
            dq.append(i)
            
        if i >= k - 1:
            if dq:
                results.append(arr[dq[0]])
            else:
                results.append(0)
    return results

if __name__ == "__main__":
    print("== Test 1 ==")
    print("arr = [-8, 2, 3, -6, 10], k = 2  ==>  " + firstNegativeInWindow([-8, 2, 3, -6, 10], 2).__str__())
    
    print("== Test 2 ==")
    print("arr = [-1, -2, -3, 5, 6, -6], k = 3  ==>  " + firstNegativeInWindow([-1, -2, -3, 5, 6, -6], 3).__str__())