k = int(input())
a = list(map(int, input().split()))

sled = 1
lst = []

for railcar in a:
    if railcar == sled:
        sled += 1
    else:
        lst.append(railcar)
    while lst and lst[-1] == sled:
        lst.pop()
        sled += 1

if not lst:
    print('YES')
else:
    print('NO')