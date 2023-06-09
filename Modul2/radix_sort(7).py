n = int(input())
arr = []
for i in range(n):
    arr.append(input())

print("Initial array: ")
for i in range(len(arr)):
    print(arr[i], end="")
    if i != len(arr) - 1:
        print(", ", end="")
print("\n**********")

phases = len(arr[0])
for i in range(phases - 1, -1, -1):
    buckets = [[] for j in range(10)]

    print("Phase", phases - i)

    for j in range(len(arr)):
        buckets[int(arr[j][i])].append(arr[j])

    for j in range(len(buckets)):
        print("Bucket", j, end=": ")
        if len(buckets[j]) == 0:
            print("empty", end='')
        for k in range(len(buckets[j])):
            print(buckets[j][k], end="")
            if k != len(buckets[j]) - 1:
                print(", ", end="")
        print()
    print("**********")

    arrInd = 0
    for j in range(10):
        for k in range(len(buckets[j])):
            arr[arrInd] = buckets[j][k]
            arrInd += 1

print("Sorted array: ")
for i in range(len(arr)):
    print(arr[i], end="")
    if i != len(arr) - 1:
        print(", ", end="")
