def find_most_frequent(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    max_freq = max(frequency.values())
    most_frequent = [num for num, freq in frequency.items() if freq == max_freq]
    return most_frequent, max_freq

# Test
arr = [4, 7, 2, 8, 4, 8, 3, 2]
result, freq = find_most_frequent(arr)
print(f"Phần tử có tần suất cao nhất là {result} với tần suất {freq}")