class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_bst(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)

    return root

def create_bst_from_array(arr):
    root = None
    for val in arr:
        root = insert_bst(root, val)
    return root

def display_tree(root, level=0):
    if root is None:
        return

    display_tree(root.right, level + 1)
    print("    " * level + str(root.val))
    display_tree(root.left, level + 1)


def search_bst(root, key):
    if root is None:
        return False

    if root.val == key:
        return True
    elif key < root.val:
        return search_bst(root.left, key)
    else:
        return search_bst(root.right, key)

def delete_bst_node(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = delete_bst_node(root.left, key)

    elif key > root.val:
        root.right = delete_bst_node(root.right, key)

    else:
        # CASE 1 & 2 handled here

        # Case 1: No child (leaf node)
        if root.left is None and root.right is None:
            return None

        # Case 2: One child
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # Case 3: Two children
        # Find inorder successor (smallest in right subtree)
        successor = find_min(root.right)
        root.val = successor.val
        root.right = delete_bst_node(root.right, successor.val)

    return root

def find_min(root):
    while root.left:
        root = root.left
    return root


arr = [50, 30, 70, 20, 40, 60, 80]

bst_root = create_bst_from_array(arr)

display_tree(bst_root)

print(search_bst(bst_root, 40))   # True
print(search_bst(bst_root, 25))   # False

root = delete_bst_node(bst_root , 70)

display_tree(root)
