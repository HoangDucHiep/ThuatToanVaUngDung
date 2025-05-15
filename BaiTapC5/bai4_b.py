import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(characters, frequencies):
    # Tạo hàng đợi ưu tiên
    priority_queue = [HuffmanNode(char, freq) for char, freq in zip(characters, frequencies)]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        # Lấy 2 nút có tần suất nhỏ nhất
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        # Tạo nút cha mới
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Thêm nút cha vào hàng đợi
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]  # Cây Huffman hoàn chỉnh

def assign_codes(node, prefix="", code_map={}):
    if node is not None:
        # Nếu là lá
        if node.char is not None:
            code_map[node.char] = prefix
        else:
            # Duyệt trái và phải
            assign_codes(node.left, prefix + "0", code_map)
            assign_codes(node.right, prefix + "1", code_map)
    return code_map

# Dữ liệu đầu vào
ch = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5, 9, 12, 13, 16, 45]

# Xây dựng cây Huffman
huffman_tree = build_huffman_tree(ch, freq)
huffman_codes = assign_codes(huffman_tree)
""" 
# In kết quả
print("Ký tự và mã Huffman:")
for char in sorted(huffman_codes.keys()):
    print(f"{char}: {huffman_codes[char]}")
 """
 
# In kết quả sắp xếp theo giá trị mã Huffman
sorted_huffman_codes = sorted(huffman_codes.items(), key=lambda item: item[1])

print("Ký tự và mã Huffman (sắp xếp theo giá trị mã):")
for char, code in sorted_huffman_codes:
    print(f"{char}: {code}")
