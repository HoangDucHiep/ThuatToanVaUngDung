class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def top(self):
        return self.heap[0] if self.heap else None

    def pop(self):
        if not self.heap: return None
        if len(self.heap) == 1: return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        smallest = index
        left, right = 2 * index + 1, 2 * index + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]: smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]: smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)


pq = PriorityQueue()
values = [8, 3, 9, 1, 7, 5, 6, 4]

for value in values:
    pq.insert(value)
    print(f"Chèn {value}: {pq.heap}")

print("\nRút các phần tử:")
while pq.heap:
    print(f"Rút {pq.pop()}: {pq.heap}")
