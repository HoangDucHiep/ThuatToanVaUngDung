def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def custom_sort(arr):
    return sorted(arr, key=lambda x: (sum_of_digits(x), x))

# Dữ liệu đầu vào
a = [43, 1, 12, 67, 33, 22, 9];

# Kết quả sau khi sắp xếp
result = custom_sort(a)
print("Kết quả sau khi sắp xếp:", result)



""" def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def radix_sort_advanced(arr):
    max_digit_sum = max(sum_of_digits(x) for x in arr)
    buckets = [[] for _ in range(max_digit_sum + 1)]

    for num in arr:
        digit_sum = sum_of_digits(num)
        buckets[digit_sum].append(num)

    for i in range(len(buckets)):
        buckets[i].sort()

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

b = [43, 1, 12, 67, 33, 22, 9];

result = radix_sort_advanced(b)
print("Kết quả sau khi sắp xếp:", result) """