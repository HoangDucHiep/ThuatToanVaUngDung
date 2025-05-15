def msd_sort(strings):
    R = 256
    def sort(a, aux, lo, hi, d):
        if hi <= lo:
            return
        count = [0] * (R + 2)
        for i in range(lo, hi + 1):
            char = ord(a[i][d]) if d < len(a[i]) else -1
            count[char + 2] += 1
        for r in range(R + 1):
            count[r + 1] += count[r]
        for i in range(lo, hi + 1):
            char = ord(a[i][d]) if d < len(a[i]) else -1
            aux[count[char + 1]] = a[i]
            count[char + 1] += 1
        for i in range(lo, hi + 1):
            a[i] = aux[i - lo]
        for r in range(R):
            sort(a, aux, lo + count[r], lo + count[r + 1] - 1, d + 1)
    aux = ["" for _ in strings]
    sort(strings, aux, 0, len(strings) - 1, 0)
    return strings

if __name__ == "__main__":
    strings = ["dab", "cab", "fab", "ebb", "acc"]
    print("MSD Sort:", msd_sort(strings))
