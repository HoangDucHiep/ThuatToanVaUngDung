##### a) 
class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def display(self):
        for i in range(self.size):
            if self.table[i]:
                print(f"Index {i}: {self.table[i]}")
            else:
                print(f"Index {i}: None")
#test
values = [4371, 1323, 6173, 4199, 4344, 9679, 1989]
hash_table = HashTableChaining(10)
for value in values:
    hash_table.insert(value)
print("Bảng băm dây chuyền:")
hash_table.display()

##### b)
class HashTableLinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            index = (index + 1) % self.size
            if index == original_index:
                print("Bảng băm đầy")
                return
        self.table[index] = key

    def display(self):
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")

# Sử dụng bảng băm thăm dò tuyến tính
hash_table_lp = HashTableLinearProbing(10)
for value in values:
    hash_table_lp.insert(value)
print("\nBảng băm thăm dò tuyến tính:")
hash_table_lp.display()

#c) 
class HashTableQuadraticProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        original_index = index
        i = 1
        while self.table[index] is not None:
            index = (original_index + i ** 2) % self.size
            i += 1
            if index == original_index:
                print("Bảng băm đầy")
                return
        self.table[index] = key

    def display(self):
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")

# Sử dụng bảng băm thăm dò bậc hai
hash_table_qp = HashTableQuadraticProbing(10)
for value in values:
    hash_table_qp.insert(value)
print("\nBảng băm thăm dò bậc hai:")
hash_table_qp.display()