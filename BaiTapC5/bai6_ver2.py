def longest_prefix_chain(words):
    # Sắp xếp danh sách từ theo độ dài tăng dần
    words.sort(key=len)
    
    # Khởi tạo danh sách chuỗi từ dài nhất
    longest_chain = []
    
    for word in words:
        # Kiểm tra nếu danh sách hiện tại rỗng hoặc từ này là tiền tố của từ cuối cùng
        if not longest_chain or longest_chain[-1] == word[:len(longest_chain[-1])]:
            longest_chain.append(word)
    
    return longest_chain

# Đầu vào: Tập hợp các từ
S = ["a", "ab", "abc", "abcd", "abcde", "b", "bc", "bcd"]
result = longest_prefix_chain(S)

print("Chuỗi từ dài nhất:", result)
