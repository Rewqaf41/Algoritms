from collections import deque

N, K = map(int, input().split())
array = list(map(int, input().split()))


window = deque()


for i in range(N):
    while window and window[0] <= i - K:
        window.popleft()

    while window and array[window[-1]] >= array[i]:
        window.pop()

    window.append(i)

    if i >= K - 1:
        print(array[window[0]])
