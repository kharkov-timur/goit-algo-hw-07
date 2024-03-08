class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_max_in_bst(root):
    if root is None:
        return None

    current = root
    while current.right:
        current = current.right

    return current.val


def find_min_in_bst(root):
    if root is None:
        return None

    current = root
    while current.left:
        current = current.left

    return current.val


def tree_sum(root):
    if root is None:
        return 0

    return root.val + tree_sum(root.left) + tree_sum(root.right)


# Створення дерева:
#       5
#      / \
#     3   7
#    / \ / \
#   1  4 6  9
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("\nМаксимальне значення у дереві:", find_max_in_bst(root))
print("Мінімальне значення у дереві:", find_min_in_bst(root))
print("Сума всіх значень у дереві:", tree_sum(root))
