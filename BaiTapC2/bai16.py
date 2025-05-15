def count_chars(s):
    char_freq = {}
    for c in s:
        if c in char_freq:
            char_freq[c] += 1
        else:
            char_freq[c] = 1
    
    result = []
    for char in sorted(char_freq.keys()):
        result.append(f"{char} {char_freq[char]}")
    
    return result

print(count_chars("aacccd"))  # ['a 2', 'c 3', 'd 1']