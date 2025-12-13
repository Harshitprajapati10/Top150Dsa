# create tree
from collections import deque

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def display_tree(root, level=0):
    if root is None:
        return
    display_tree(root.right, level + 1)
    print("    " * level + str(root.val))
    display_tree(root.left, level + 1)

# level order traversal
def lvlorderTraversal(root):
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        result.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return result

# preorder traversal
# NLR
def preOrder(root):
    if root == None:
        return
    print(root.val, end =" ")
    preOrder(root.left)
    preOrder(root.right)

# INorder traversal
#LNR
def InOrder(root):
    if root == None:
        return
    InOrder(root.left)
    print(root.val ,end = " ")
    InOrder(root.right)

# postorder traversal # LRN
def postOrder(root):
    if root == None:
        return 
    postOrder(root.left)
    postOrder(root.right)
    print(root.val , end = " ")


# ------------------------
# Iterative DFS
def dfs_preorder_iterative(root):
    # process node, pushright then left so that left comes first
    if not root:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def dfs_inorder_iterative(root):
    # go left as much , process node, move right
    if not root:
        return []
    stack = []
    result = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result


def dfs_postorder_iterative(root):
    if not root: return []
    stack1 = [root]
    stack2 =[]
    result = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        result.append(stack2.pop().val)
    return result



# WAF to count total number of leaf nodes in given BT
def get_total_leaf_node(root):
    if root is not None:
        if root.left is None and root.right is None:
            return 1
        else:
            return get_total_leaf_node(root.left) + get_total_leaf_node(root.right)
    return 0



# WAF to count total number of internal nodes
def get_total_internal_nodes(root):
    if root is not None:
        if root.left is None and root.right is None:
            return 0
        else:
            return 1 + get_total_internal_nodes(root.left) + get_total_internal_nodes(root.right)
    return 0


# WAF to count total Nodes
def get_total_nodes(root):
    if root is not None:
        if root.left is None and root.right is None:
            return 1
        else:
            return 1 + get_total_nodes(root.left) + get_total_nodes(root.right)
    return 0

# WAF to count total number of null links in internal nodes
def get_total_null_links_internal_nodes(root):
    if root is not None:
        if root.left is None and root.right is None:
            return 0
        else:
            count = 0
            if root.left is None:
                count += 1
            if root.right is None:
                count += 1
            return (
                count
                + get_total_null_links_internal_nodes(root.left)
                + get_total_null_links_internal_nodes(root.right)
            )
    return 0

# 226 invert binary tree
def invertTree(root):
    if root is None:
        return None
    left = invertTree(root.left)
    right = invertTree(root.right)
    root.left = right
    root.right = left
    return root


#104 -> max depth of the binary treee
def maxDepth(root):
    if root is None: return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


# 543 -> diameter of the binary tree
class getDiameter:
    def __init__(self):
        self.diameter = 0
    def height(self,root):
        if root in None: return 0
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        self.diameter = max(self.diameter, leftHeight + rightHeight)
        return max(leftHeight, rightHeight) + 1
    def diameter_of_binary_tree(self,root):
        return self.diameter


#110 balanced binary tree  
def isBalancedTree(node):
    def height(root):
        if root is None:
            return True
        leftHeight = height(root.left)
        if leftHeight == -1:
            return -1
        rightHeight = height(root.right)
        if rightHeight == -1:
            return -1
        if abs(leftHeight-rightHeight)>1:
            return -1
        return (1 + max(leftHeight,rightHeight))
    return height(node) != -1


# 100 same Tree
# waf boolean to check whether two trees are same
def same_tree(p,q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return (same_tree(p.left,q.left) and
                same_tree(p.right,q.right))

#572 subtree of a tree
def isSubtree(root, subRoot):
        if not subRoot: return True
        if not root: return False
        if same_tree(root,subRoot):
            return True
        return (isSubtree(root.left, subRoot) or
                isSubtree(root.right,subRoot))


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.right = TreeNode(6)

    """
        1
       / \
      2   3
     / \   \
    4   5   6

    """

    display_tree(root)
    print("BFS is: ", lvlorderTraversal(root))
    print("\nPreOrder is: ")
    preOrder(root)
    print("\nInOrder is: ")
    InOrder(root)
    print("\nPostOrder is: ")
    postOrder(root)
    print("\nPreorder iterative is:")
    print(dfs_preorder_iterative(root))
    print("\INorder iterative is:")
    print(dfs_inorder_iterative(root))
    print("\INorder iterative is:")
    print(dfs_inorder_iterative(root))
    print("\PostOrder iterative is:")
    print(dfs_postorder_iterative(root))
    print("\n\ntotal leaf nodes: ", get_total_leaf_node(root))
    print("\n\ntotal internal nodes: ", get_total_internal_nodes(root))
    print("\n\ntotal nodes: ", get_total_nodes(root))
    print("\n\n Total null links in internal node : ", get_total_null_links_internal_nodes(root))

    print("\n\nInverted Binary tree is: ", display_tree(invertTree(root)))
    print("\n\n Depth is : ", maxDepth(root))

    o = getDiameter()
    dia = o.diameter_of_binary_tree(root)
    print(dia)
