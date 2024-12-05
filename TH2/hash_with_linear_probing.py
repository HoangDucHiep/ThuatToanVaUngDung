class linear_probing_hash_table_dict:
    def __init__(self, size = 23):
        self.size = size
        self.table = [None] * size
        
    def _hash_function(self, key):
        ascii_sum = sum(ord(char) for char in key)
        return ascii_sum % self.size

    def insert(self, word, meaning):
        index = self._hash_function(word)
        
        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] is None or self.table[new_index][0] == word:
                self.table[new_index] = (word, meaning)
                return
        
            
        print("Hash table is full, cannot insert")

    def get(self, word):
        index = self._hash_function(word)

        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] is None:
                return None 
            if self.table[new_index][0] == word:
                return self.table[new_index][1]

        return None 

    def display(self):
        for i, item in enumerate(self.table):
            if item is None:
                print(f"Index {i}: Empty")
            else:
                print(f"Index {i}: {item}")
hash_table_linear = linear_probing_hash_table_dict()

hash_table_linear.insert('apple', 'quả táo')
hash_table_linear.insert('banana', 'quả chuối')
hash_table_linear.insert('grape', 'quả nho')
hash_table_linear.insert('watermelon', 'quả dưa hấu')

print("Meaning of 'apple':", hash_table_linear.get('apple'))
print("Meaning of 'banana':", hash_table_linear.get('banana'))
print("Meaning of 'grape':", hash_table_linear.get('grape'))
print("Meaning of 'watermelon':", hash_table_linear.get('watermelon'))

hash_table_linear.display()
