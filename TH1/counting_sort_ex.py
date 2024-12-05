def counting_sort(arr):
    max_val = max(arr)
    
    # Create a list of 0s with length max_val + 1
    count = [0] * (max_val + 1)
    
    # Count the number of times each element appears
    for num in arr:
        count[num] += 1
        
    # Create a new list to store the sorted elements
    sorted_arr = []
    
    # Iterate over the count list and add the elements to the sorted list
    for i in range(len(count)):
        sorted_arr.extend(count[i] * [i])
        
    return sorted_arr

def find_mode(arr):
    max_val = max(arr)
    
    # Create a list of 0s with length max_val + 1
    count = [0] * (max_val + 1)
    
    # Count the number of times each element appears
    for num in arr:
        count[num] += 1
    
    mode = count.index(max(count))
    
    # Create a new list to store the sorted elements
    sorted_arr = []
    
    # Iterate over the count list and add the elements to the sorted list
    for i in range(len(count)):
        sorted_arr.extend(count[i] * [i])
        
    if len(sorted_arr) % 2 == 0:
        median = (sorted_arr[len(sorted_arr) // 2] + sorted_arr[len(sorted_arr) // 2 - 1]) / 2
    else:
        median = sorted_arr[len(sorted_arr) // 2]
        
    return mode, median

# Example usage
arr = [1, 4, 1, 2, 7, 1, 2, 5, 3, 6]

mode, median = find_mode(arr)
sorted_arr = counting_sort(arr)
print("Array: " + str(arr))
print("Sorted Array: " + str(sorted_arr))
print("Mode:", mode)
print("Median:", median)