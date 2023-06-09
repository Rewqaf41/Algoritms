def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def build_segment_tree(arr, left, right, segment_tree, node):
    if left == right:
        segment_tree[node] = arr[left]
        return segment_tree

    mid = (left + right) // 2

    segment_tree = build_segment_tree(arr, left, mid, segment_tree, 2 * node + 1)
    segment_tree = build_segment_tree(arr, mid + 1, right, segment_tree, 2 * node + 2)

    segment_tree[node] = gcd(segment_tree[2 * node + 1], segment_tree[2 * node + 2])

    return segment_tree

def get_gcd(segment_tree, node, node_left, node_right, left_bound, right_bound):
    if left_bound <= node_left and right_bound >= node_right:
        return segment_tree[node]

    if right_bound < node_left or left_bound > node_right:
        return 0

    mid = (node_left + node_right) // 2

    left_gcd = get_gcd(segment_tree, 2 * node + 1, node_left, mid, left_bound, right_bound)
    right_gcd = get_gcd(segment_tree, 2 * node + 2, mid + 1, node_right, left_bound, right_bound)

    return gcd(left_gcd, right_gcd)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())

    segment_tree = build_segment_tree(arr, 0, n - 1, [0] * (n * 4), 0)
    answ = []

    for _ in range(k):
        query = list(map(int, input().split()))
        left_bound = query[0] - 1
        right_bound = query[1] - 1

        answ.append(get_gcd(segment_tree, 0, 0, n - 1, left_bound, right_bound))

    print(*answ)
    
    