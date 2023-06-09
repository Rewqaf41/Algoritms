s = input()
lst = []
count = 0

for n in s:
    if n == "(":
        lst.append(n)
    else:
        if len(lst) > 0 and lst[-1] == "(":
            lst.pop()
        else:
            count += 1

count += len(lst)
print(count)