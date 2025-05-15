def is_prefix(u, v):
    return v.startswith(u)

def longest_chain(words):
    words.sort()
    n = len(words)
    dp = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if is_prefix(words[j], words[i]) and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_length = max(dp)
    end_index = dp.index(max_length)

    chain = []
    while end_index != -1:
        chain.append(words[end_index])
        end_index = prev[end_index]

    return list(reversed(chain))

# Ví dụ:
S = ["a", "ab", "abc", "abcd", "abcde", "b", "bc", "bcd"]
result = longest_chain(S)
print("Chuỗi từ dài nhất:", result)