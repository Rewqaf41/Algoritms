def compute_prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


def find_cyclic_shift(s, t):
    n = len(s)
    m = len(t)
    if n != m:
        return -1
    s = s + "#" + t + t
    pi = compute_prefix_function(s)
    for i in range(n):
        if pi[i + m + 1] == m:
            return i
    return -1
