n = int(input())
lst_add = input()
split_lst = lst_add.split(" ")
lst = []
for el in split_lst:
    lst.append(int(el))
count = 0
for i in range(n - 1):
    for j in range(n - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            count += 1
            print(" ".join(map(str, lst)))
if count == 0:
    print(0)
