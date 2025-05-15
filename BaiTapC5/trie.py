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

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def delete(self, word):
        def _delete(node, word, depth):
            if not node:
                return False
            if depth == len(word):
                if node.is_end_of_word:
                    node.is_end_of_word = False
                return not bool(node.children)
            char = word[depth]
            if _delete(node.children.get(char), word, depth + 1):
                del node.children[char]
                return not node.children and not node.is_end_of_word
            return False
        _delete(self.root, word, 0)
        
if __name__ == "__main__":
    trie = Trie()
    trie.insert("hello")
    trie.insert("world")
    print("Search 'hello':", trie.search("hello"))
    print("Search 'python':", trie.search("python"))
