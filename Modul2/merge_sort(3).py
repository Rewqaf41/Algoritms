def merge(arr1, arr2):
    count1 = 0
    count2 = 0
    arrRes = [0] * (len(arr1) + len(arr2))
    for i in range(len(arrRes)):
        if count1 == len(arr1):
            arrRes[i] = arr2[count2]
            count2 += 1
        elif count2 == len(arr2):
            arrRes[i] = arr1[count1]
            count1 += 1
        elif arr1[count1] <= arr2[count2]:
            arrRes[i] = arr1[count1]
            count1 += 1
        else:
            arrRes[i] = arr2[count2]
            count2 += 1

    return arrRes

def mergeSort(arr, left, right):
    if right-left == 1:
        return [arr[left]]

    middle = (left + right) // 2
    leftPart = mergeSort(arr, left, middle)
    rightPart = mergeSort(arr, middle, right)

    res = merge(leftPart, rightPart)

    print(left+1, right, res[0], res[-1])

    return res

n = int(input())
arr = [int(x) for x in input().split()]

arr = mergeSort(arr, 0, n)
print(*arr)
