def check_sum(arr, sum):
    num_dict = {}
    for i, num in enumerate(arr):
        needed = sum - num
        if needed in num_dict:
            return True
        num_dict[num] = i
    return False

print(check_sum([2, 4, -1, 9, 8], 6))
print(check_sum([2, 5, 3, 8, 9], 3))