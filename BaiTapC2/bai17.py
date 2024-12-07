def modify_string(s):
    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    
    char_freq = [(char, freq[char]) for char in set(s)]
    char_freq.sort(key=lambda x: (-x[1], x[0]))
    
    result = ''.join(char for char, _ in char_freq)
    
    return result

# Test
print(modify_string("codelearn"))  # eacdlnor
print(modify_string("helloworld"))  # lodehrw