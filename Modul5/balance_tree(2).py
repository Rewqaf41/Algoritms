class Tree:
    def init(self, val):
        self.val = val
        self.l = None
        self.r = None


def insert(root, val):
    if root is None:
        return Tree(val)
    elif val < root.val:
        root.l = insert(root.l, val)
    elif val > root.val:
        root.r = insert(root.r, val)
    return root


def build_tree(arr):
    root = None
    for i in range(len(arr)):
        root = insert(root, arr[i])
    return root


def height(tree):
    if tree is None:
        return 0
    else:
        return max(height(tree.l), height(tree.r)) + 1


def is_balanced(tree):
    if tree is None:
        return True
    left_height = height(tree.l)
    right_height = height(tree.r)
    if abs(left_height - right_height) > 1:
        return False
    return is_balanced(tree.l) and is_balanced(tree.r)


if __name__ == "__main__":
    sarr = input().split()
    arr = [int(sarr[i]) for i in range(len(sarr) - 1)]

    tree = build_tree(arr)

    if is_balanced(tree):
        print("YES")
    else:
        print("NO")