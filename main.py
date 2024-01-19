import random


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def find_min(root):
    node = root
    while node.left:
        node = node.left
    return node.val


def find_max(root):
    node = root
    while node.right:
        node = node.right
    return node.val


def find_sum(root):
    if root is None:
        return 0
    return root.val + find_sum(root.left) + find_sum(root.right)


def main():
    root = Node(random.randint(1, 20))
    for i in range(0, 10):
        root = insert(root, random.randint(1, 20))

    print("\nMy binary tree\n", root)

    print("Minimum value: ",  find_min(root), '\n')
    print("Maximum value: ",  find_max(root), '\n')
    print("Sum value: ",  find_sum(root), '\n')


if __name__ == "__main__":
    main()
