class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insert(root, val)
    else:
        root.right = insert(root, val)
    return root


def search(root, val):
    if not root or root.val == val:
        return root

    if root.val < val:
        return search(root.right, val)
    else:
        return search(root.left, val)