a = int(input())
b = list(map(int, input().split()))

lst = []
an = [-1] * a

for k in range(a - 1, -1, -1):
    while lst and lst[-1][0] >= b[k]:
        lst.pop()

    if lst:
        an[k] = lst[-1][1]

    lst.append((b[k], k))

print(*an)