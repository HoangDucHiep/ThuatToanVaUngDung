from heapq import heappush, heappop

def findProducts(A):
    heap = []  # max 3 elems
    result = []

    for x in A:
        heappush(heap, x)
        if len(heap) > 3:
            heappop(heap)  # remove the smallest one

        if len(heap) < 3:
            result.append(-1)
        else:
            product = 1
            for num in heap:
                product *= num
            result.append(product)

    return result

# Test
A = [1, 2, 3, 3, 1, 4]
print(findProducts(A))
