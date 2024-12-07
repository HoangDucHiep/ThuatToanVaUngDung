def count_frequency(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    sorted_frequency = dict(sorted(frequency.items()))
    return sorted_frequency

# Ví dụ sử dụng
arr = [4, 2, 2, 8, 3, 3, 3, 1]
result = count_frequency(arr)
print(result)