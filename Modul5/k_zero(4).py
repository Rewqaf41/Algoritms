import bisect

N = int(input())
arr = list(map(int, input().split()))
Q = int(input())

prefix_zeros = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_zeros[i] = prefix_zeros[i - 1] + (arr[i - 1] == 0)

for _ in range(Q):
    l, r, k = map(int, input().split())

    zeros_count = prefix_zeros[r] - prefix_zeros[l - 1]

    if zeros_count < k:
        print(-1, end=" ")
    else:
        zero_index = bisect.bisect_left(prefix_zeros, prefix_zeros[l - 1] + k)
        print(zero_index, end=" ")