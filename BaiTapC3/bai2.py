def counting_sort_find_mode_median(arr):
    max_value = max(arr)
    min_value = min(arr)
    range_of_values = max_value - min_value + 1

    count = [0] * range_of_values
    for num in arr:
        count[num - min_value] += 1

    cumulative_count = [0] * range_of_values
    cumulative_count[0] = count[0]
    for i in range(1, range_of_values):
        cumulative_count[i] = cumulative_count[i - 1] + count[i]

    sorted_array = [0] * len(arr)
    for num in reversed(arr):
        sorted_array[cumulative_count[num - min_value] - 1] = num
        cumulative_count[num - min_value] -= 1

    mode = None
    max_frequency = max(count)
    for i, freq in enumerate(count):
        if freq == max_frequency:
            mode = i + min_value
            break

    n = len(sorted_array)
    if n % 2 == 1:
        median = sorted_array[n // 2]
    else:
        median = (sorted_array[n // 2 - 1] + sorted_array[n // 2]) / 2

    return mode, median, sorted_array

A = [1, 4, 1, 2, 7, 1, 2, 5, 3, 6]
mode, median, sorted_A = counting_sort_find_mode_median(A)

print("Mảng đã sắp xếp:", sorted_A)
print("Mốt:", mode)
print("Trung vị:", median)


""" my one
def find_mode(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    
    mode = count.index(max(count))
    sorted_arr = []
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
print("Array: " + str(arr))
print("Sorted Array: " + str(sorted_arr))
print("Mode:", mode)
print("Median:", median) 
"""