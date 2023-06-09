def twice_sort():
    n = int(input())
    lst = []

    for i in range(n):
        twice = input().split()
        lst.append(list(map(int, twice)))
    for i in range(n):
        for j in range(n - 1):
            if lst[j][1] < lst[j + 1][1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            elif lst[j][1] == lst[j + 1][1]:
                if lst[j][0] > lst[j + 1][0]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]

    for i in range(n):
        print(lst[i][0], " ", lst[i][1], end="\n", sep="")


twice_sort()
