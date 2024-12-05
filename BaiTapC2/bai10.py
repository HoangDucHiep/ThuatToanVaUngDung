import heapq
import math

def find_k_nearest_dorms(dorms, k):
    nearest_dorms = []
    
    for dorm in dorms:
        distance = math.sqrt(dorm[0]**2 + dorm[1]**2)
        if len(nearest_dorms) < k:
            heapq.heappush(nearest_dorms, (-distance, dorm))
        else:
            if -distance > nearest_dorms[0][0]:
                heapq.heapreplace(nearest_dorms, (-distance, dorm))
    return [dorm for (_, dorm) in sorted(nearest_dorms, key=lambda x: -x[0])]

def test_k_nearest_dorms():
    dorms = [(1, 0), (2, 1), (3, 6), (-5, 2), (1, -4)]
    k = 3
    result = find_k_nearest_dorms(dorms, k)
    print("K ký túc xá gần nhất:")
    for dorm in result:
        distance = math.sqrt(dorm[0]**2 + dorm[1]**2)
        print(f"Dorm {dorm} - Khoảng cách: {distance:.2f}")

test_k_nearest_dorms()