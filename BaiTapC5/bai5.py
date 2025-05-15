def is_prefix(str1, str2):
    return str2.startswith(str1)

def solve():
    N = int(input())
    strings = [input().strip() for _ in range(N)]
    strings.sort()
    for i in range(1, N):
        if is_prefix(strings[i-1], strings[i]):
            print("BAD SET")
            print(strings[i])
            return
    print("GOOD SET")

solve()