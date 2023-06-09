def find_repeats(s):
    for i in range(1, len(s) // 2 + 1):
        if len(s) % i == 0 and s[:i] * (len(s) // i) == s:
            return len(s) // i
    return 1

s = input().strip()
k = find_repeats(s)
print(k)