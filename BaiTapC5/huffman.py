import heapq
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(frequencies):
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    root = heap[0]
    def build_code(node, code, result):
        if node:
            if node.char is not None:
                result[node.char] = code
            build_code(node.left, code + "0", result)
            build_code(node.right, code + "1", result)
    result = {}
    build_code(root, "", result)
    return result

# Example usage
if __name__ == "__main__":
    frequencies = {"a": 5, "b": 9, "c": 12, "d": 13, "e": 16, "f": 45}
    codes = huffman_encoding(frequencies)
    print("Huffman Codes:", codes)
