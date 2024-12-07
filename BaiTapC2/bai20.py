def largest_element(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    min_freq = min(freq.values())
    result = max(num for num, count in freq.items() if count == min_freq)
    return result

# Test cases
print(largest_element([2,2,4,4,7,7,7]))  # 4
print(largest_element([1,3,4,5,5]))      # 4