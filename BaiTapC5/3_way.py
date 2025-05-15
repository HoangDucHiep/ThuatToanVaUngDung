def three_way_quick_sort(strings):
    def sort(a, lo, hi, d):
        if hi <= lo:
            return
        lt, gt = lo, hi
        v = ord(a[lo][d]) if d < len(a[lo]) else -1
        i = lo + 1
        
        while i <= gt:
            t = ord(a[i][d]) if d < len(a[i]) else -1
            if t < v:
                a[lt], a[i] = a[i], a[lt]
                lt += 1
                i += 1
            elif t > v:
                a[i], a[gt] = a[gt], a[i]
                gt -= 1
            else:
                i += 1
        sort(a, lo, lt - 1, d)
        if v >= 0:
            sort(a, lt, gt, d + 1)
        sort(a, gt + 1, hi, d)
        
    sort(strings, 0, len(strings) - 1, 0)
    return strings

if __name__ == "__main__":
    strings = ["dab", "cab", "fab", "ebb", "acc"]
    print("3-way Quick Sort:", three_way_quick_sort(strings))
