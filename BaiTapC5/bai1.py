import unicodedata

def viet_char_order(char):
    base_order = {
        'a': 1, 'ă': 2, 'â': 3, 
        'e': 4, 'ê': 5, 
        'i': 6, 
        'o': 7, 'ô': 8, 'ơ': 9, 
        'u': 10, 'ư': 11, 
        'y': 12, 
        'd': 13, 'đ': 14
    }

    tone_order = {
        '': 0,   # Không dấu
        '̀': 1,  # Huyền
        '̉': 2,  # Hỏi
        '́': 3,  # Sắc
        '̃': 4,  # Ngã
        '̣': 5   # Nặng
    }

    decomposed = unicodedata.normalize('NFD', char)
    base_char = decomposed[0]
    tone = ''.join(c for c in decomposed[1:] if unicodedata.combining(c))
    base_value = base_order.get(base_char, 100)
    tone_value = tone_order.get(tone, 100)
    return (base_value, tone_value)

def viet_string_order(s):
    return [viet_char_order(char) for char in s]

def viet_sort(strings):
    return sorted(strings, key=viet_string_order)

# Ví dụ sử dụng
strings = ["Hoa", "Hỏa", "Hõa", "Họa", "Hòa", "Hóa"]
sorted_strings = viet_sort(strings)
print("Kết quả sắp xếp:", sorted_strings)