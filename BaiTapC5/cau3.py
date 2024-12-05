class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def longest_common_prefix(self):
        prefix = ""
        node = self.root
        while node and not node.is_end_of_word and len(node.children) == 1:
            char, next_node = next(iter(node.children.items()))
            prefix += char
            node = next_node
        return prefix

def longest_common_prefix(strings):
    trie = Trie()
    for word in strings:
        trie.insert(word)
    return trie.longest_common_prefix()

# Ví dụ sử dụng
s = ["flower", "flow", "flour"]
print("Tiền tố chung dài nhất là:", longest_common_prefix(s))
