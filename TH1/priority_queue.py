

class priority_queue:
    """A priority queue implemented as a binary heap"""

    def __init__(self):
        self.heap = [0]
        self.size = 0
        
    def is_empty(self):
        return self.size == 0
        
    def insert(self, val):
        self.heap.append(val)
        self.size += 1
        self.swim_up(self.size)
        
    def swim_up(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2
            
    def del_min(self):
        min_val = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink_down(1)
        return min_val
    
    def sink_down(self, i):
        while i * 2 <= self.size:
            mc = self.min_child(i)
            if self.heap[i] > self.heap[mc]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc
            
    def min_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heap[i * 2] < self.heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

#main 
if __name__ == "__main__":
    pq = priority_queue()
    pq.insert(3)
    pq.insert(2)
    pq.insert(1)
    pq.insert(5)
    pq.insert(4)
    print(pq.del_min())
    print(pq.del_min())
    print(pq.del_min())
    print(pq.del_min())
    print(pq.del_min())
    
    arr = [3, 2, 1, 5, 4]
    
    while (not pq.is_empty()):
        print(pq.del_min())
    