###### a) 
class HashDictionaryChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def display(self):
        for i in range(self.size):
            if self.table[i]:
                print(f"Index {i}: {self.table[i]}")
            else:
                print(f"Index {i}: None")

###### b) 
class HashDictionaryLinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
            if index == original_index:
                return
        self.table[index] = (key, value)

    def get(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                return None
        return None

    def display(self):
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")


###### c)
class HashDictionaryQuadraticProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        original_index = index
        i = 1

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (original_index + i ** 2) % self.size
            i += 1
            if index == original_index:
                raise Exception("Bảng băm đầy")
        self.table[index] = (key, value)

    def get(self, key):
        index = self.hash_function(key)
        original_index = index
        i = 1

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (original_index + i ** 2) % self.size
            i += 1
            if index == original_index:
                break
        return None

    def display(self):
        for i in range(self.size):
            if self.table[i] is not None:
                print(f"Index {i}: {self.table[i]}")
            else:
                print(f"Index {i}: None")

# Sử dụng từ điển dựa trên bảng băm với thăm dò bậc hai
hash_dict_qp = HashDictionaryLinearProbing(10)
values = [(4371, 'A'), (1323, 'B'), (6173, 'C'), (4199, 'D'), (4344, 'E'), (9679, 'F'), (1989, 'G')]
for key, value in values:
    hash_dict_qp.insert(key, value)

print("Từ điển (Hash Table) với thăm dò bậc hai:")
hash_dict_qp.display()

print("\nLấy giá trị của key 1323:", hash_dict_qp.get(1323))
print("Lấy giá trị của key 9999:", hash_dict_qp.get(9999))