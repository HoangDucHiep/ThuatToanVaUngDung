class UnorderedMap:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def get(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None

    def remove(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size
            if index == original_index:
                break

    def display(self):
        for i in range(self.size):
            if self.table[i] is not None:
                print(f"Index {i}: {self.table[i]}")
            else:
                print(f"Index {i}: None")

# Sử dụng unordered_map
unordered_map = UnorderedMap(10)
unordered_map.insert(4371, 'A')
unordered_map.insert(1323, 'B')
unordered_map.insert(6173, 'C')
unordered_map.insert(4199, 'D')
unordered_map.insert(4344, 'E')
print("Unordered Map:")
unordered_map.display()
print("\nLấy giá trị của key 1323:", unordered_map.get(1323))
print("Lấy giá trị của key 9999:", unordered_map.get(9999))
unordered_map.remove(1323)
print("\nUnordered Map sau khi xóa key 1323:")
unordered_map.display()