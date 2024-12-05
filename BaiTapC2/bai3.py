def turn_to_k_distinct_char(str, k):
    char_set = set(str)
    if (str.__len__() < k):  #if the original string has less than k distinct characters
        return "impossible"  # it is impossible to turn it into a string with k distinct characters
    else:
        return abs(char_set.__len__() - k)  # else, that is the difference between the number of distinct characters and k

if __name__ == "__main__":
    print("=== Tets 1 ===")
    print("text: codelearn, k = 9 => " + turn_to_k_distinct_char("codelearn", 9).__str__()) # 1
    print("=== Tets 2 ===")
    print("text: google, k = 7 => " + turn_to_k_distinct_char("google", 7).__str__()) # impossible
    print("=== Tets 3 ===")
    print("text: codelearn, k = 3 => " + turn_to_k_distinct_char("codelearn", 3).__str__()) # 5