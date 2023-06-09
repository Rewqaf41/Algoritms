str1 = input('')
str2 = input('')
result = []
start = 0
stop = len(str2)
for i in range(len(str1)-len(str2)+1):
    if str2 == str1[start:stop]:
        result.append(start)
    start += 1
    stop += 1
s = ' '.join(str(x) for x in result)
print(s)