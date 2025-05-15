class UnorderedSet:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)

        while self.table[index] is not None:
            if self.table[index] == key:
                return
            index = (index + 1) % self.size

        self.table[index] = key

    def contains(self, key):
        index = self.hash_function(key)
        original_index = index

        while self.table[index] is not None:
            if self.table[index] == key:
                return True
            index = (index + 1) % self.size
            if index == original_index:
                break

        return False

    def remove(self, key):
        index = self.hash_function(key)
        original_index = index

        # Tìm key để xóa
        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index] = None  # Xóa phần tử
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

unordered_set = UnorderedSet(10)
unordered_set.insert(4371)
unordered_set.insert(1323)
unordered_set.insert(6173)
unordered_set.insert(4199)
unordered_set.insert(4344)
print("Unordered Set:")
unordered_set.display()
print("\nKiểm tra sự tồn tại của 1323:", unordered_set.contains(1323))  # True
print("Kiểm tra sự tồn tại của 9999:", unordered_set.contains(9999))  # False
unordered_set.remove(1323)
print("\nUnordered Set sau khi xóa 1323:")
unordered_set.display()
