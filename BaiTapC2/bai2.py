import heapq
def sec_min(arr) -> str:
    temp_set = set(arr)     # create a set to remove duplicate elements
        
    if temp_set.__len__() < 2:  # if the number of elements is less than 2, 
        return "No"             # means there is no second minimum element
    
    # use heap pq to find the second minimum element
    heap = []
    for num in temp_set:
        heapq.heappush(heap, num)
    return heap[1].__str__()

if __name__ == "__main__":
    print("=== Tets 1 ===")
    print("arr = [3, 1, 2, 1, 1] => " + sec_min([3, 1, 2, 1, 1])) # 2
    print("=== Tets 2 ===")
    print("arr = [1, 1, 1, 1, 1] => " + sec_min([1, 1, 1, 1, 1])) # No
    print("=== Tets 3 ===")
    print("arr = [1, 2, 3, 4, 5] => " + sec_min([1, 2, 3, 4, 5])) # 2
