# https://leetcode.com/problems/inorder-successor-in-bst-ii/
# Difficulty: Medium
# Tags: tree binary_tree bst inorder successor

# Problem
# Given a node in a binary search tree, return the in-order successor of that node in the BST. If that node has no in-order successor, return null.

# The successor of a node is the node with the smallest key greater than node.val.

# You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node:

# class Node {
#     public int val;
#     public Node left;
#     public Node right;
#     public Node parent;
# }

# Solution
# Time O(n) and space O(n)
# We can either use solution 1: Exploring all the edge cases, we find that the successor of a node can be either:
# IF RIGHT NODE EXIST:
# 1) The right node if it has no left nodes.
# 2) The left-most node of a right node, otherwise.
# IF IT DOESN'T, IT MUST BE IN PARENT NODES:
# 1) If parent node equals to it's right node, we move to parent.
# 2) Otherwise, the successor is just a parent node.

# Solution 2: Move to the top unless you are at the root. Then use inorder traversal to find the successor of a node (same as in a previous problem).

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


def inorderSuccessor(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node

    while node.parent and node == node.parent.right:
        node = node.parent
    return node.parent

    # --- or ---


def inorderSuccessor(node):
    root = node
    while root.parent:
        root = root.parent

    stack = []
    curr = root
    found = False

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()

        if found:
            return curr
        if curr.val == node.val:
            found = True

        curr = curr.right

    return None
