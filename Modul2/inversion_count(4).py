def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])
    merged, inv_merge = merge(left, right)
    return merged, inv_left + inv_right + inv_merge


def merge(left, right):
    merged = []
    i, j = 0, 0
    inversions = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i
    merged += left[i:]
    merged += right[j:]
    return merged, inversions


n = int(input())
arr = list(map(int, input().split()))
inversions = merge_sort(arr)
print(inversions[1])