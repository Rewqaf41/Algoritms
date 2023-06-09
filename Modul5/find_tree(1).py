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

def print_singles_id(root):
    nodes = []

    if root is None:
        return

    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        if (node.l is not None and node.r is None) or (node.l is None and node.r is not None):
            nodes.append(node.val)
        if node.l is not None:
            stack.append(node.l)
        if node.r is not None:
            stack.append(node.r)

    nodes.sort()

    for i in range(len(nodes)):
        print(nodes[i])


if __name__ == "__main__":
    sarr = input().split()
    arr = [int(sarr[i]) for i in range(len(sarr) - 1)]

    tree = build_tree(arr)

    print_singles_id(tree)