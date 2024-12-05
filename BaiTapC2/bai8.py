from collections import deque

def tide(arr, n):
    dq = deque(arr)
    
    for i in range(n):
        k = dq.popleft()
        dq.extend([k, k])
        print(dq)
    
    return dq[0]

if __name__ == "__main__":
    print(tide([1, 2, 3 ,4 ,5], 6))