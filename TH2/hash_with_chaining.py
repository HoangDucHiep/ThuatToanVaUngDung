class hash_table_dict:
    """ init a hash_table_dict with default size 23 """
    def __init__(self, size=23):
        self.size = size
        self.table = [[] for _ in range(size)] 
        
    def _hash_function(self, key):
        """ hash function, return hashed index in table """
        ascii_sum = sum(ord(char) for char in key)
        return ascii_sum % self.size

    def insert(self, word, meaning):
        """ insert an item into hash table """
        index = self._hash_function(word)
        for pair in self.table[index]:
            # check if the word exists in the table """
            if pair[0] == word:
                # if it does, up date the word """
                pair[1] = meaning
                return
        #else, append new word
        self.table[index].append((word, meaning))

    def get(self, word):
        """ Get a meaning by a word """
        index = self._hash_function(word)
        for pair in self.table[index]:
            if pair[0] == word:
                return pair[1]  # return the meaning of the word
        #return none if can't find the word
        return None

    def display(self):
        for i, chain in enumerate(self.table):
            if chain:
                print(f"Index {i}: {chain}")
            else:
                print(f"Index {i}: Empty")

hash_table_dict = hash_table_dict()

hash_table_dict.insert('apple', 'quả táo')
hash_table_dict.insert('banana', 'quả chuối')
hash_table_dict.insert('grape', 'quả nho')
hash_table_dict.insert('watermelon', 'quả dưa hấu')

print("Meaning of 'apple':", hash_table_dict.get('apple'))
print("Meaning of 'banana':", hash_table_dict.get('banana'))
print("Meaning of 'grape':", hash_table_dict.get('grape'))
print("Meaning of 'watermelon':", hash_table_dict.get('watermelon'))


hash_table_dict.display()
