def sum_of_common(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    
    common = set1.intersection(set2)
    
    result = sum(common)
    return result

# Test
arr1 = [6, 7, 5, 4, 6, 8]
arr2 = [2, 5, 7, 5, 3]
print(sum_of_common(arr1, arr2))  # 12

arr1 = [5, 6, 7]
arr2 = [2, 3, 4]
print(sum_of_common(arr1, arr2))  # 0