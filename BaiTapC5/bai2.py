def vietnamese_char_order():
    base_chars = "aăâbcdđeêghiklmnoôơpqrstuưvxy"
    accents = ["", "̀", "̉", "́", "̃", "̣"]  # Không dấu, huyền, hỏi, sắc, ngã, nặng
    order = {}
    
    idx = 0
    for char in base_chars:
        for accent in accents:
            order[char + accent] = idx
            idx += 1
    
    return order

def encode_vietnamese_string(string, order):
    return [order.get(char, -1) for char in string.lower()]  # -1 cho ký tự không hợp lệ

def sort_vietnamese_strings(strings):
    order = vietnamese_char_order()
    return sorted(strings, key=lambda s: encode_vietnamese_string(s, order))

# Ví dụ:
strings = ["Hòa", "Hoa", "Hỏa", "Hóa", "Hõa", "Họa"]
sorted_strings = sort_vietnamese_strings(strings)
print("Danh sách đã sắp xếp:", sorted_strings)