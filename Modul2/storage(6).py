n = int(input())
stock = list(map(int, input().split()))
k = int(input())
orders = list(map(int, input().split()))

count = [0] * n
for order in orders:
    count[order - 1] += 1

for i in range(n):
    count[i] -= stock[i]
    if count[i] > 0:
        print("yes")
    else:
        print("no")