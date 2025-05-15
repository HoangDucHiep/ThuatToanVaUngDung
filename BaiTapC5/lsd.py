def lsd_sort(strings, W):
    R = 256
    N = len(strings)
    aux = ["" for _ in range(N)]

    for d in range(W - 1, -1, -1):
        count = [0] * (R + 1)
        for s in strings:
            count[ord(s[d]) + 1] += 1
        for r in range(R):
            count[r + 1] += count[r]
        for s in strings:
            aux[count[ord(s[d])]] = s
            count[ord(s[d])] += 1

        strings = aux[:]
    return strings

if __name__ == "__main__":
    strings = ["dab", "cab", "fab", "ebb", "acc"]
    print("LSD Sort:", lsd_sort(strings, 3))
    