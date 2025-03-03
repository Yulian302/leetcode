# https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Difficulty: Medium
# Tags: tree bst insertion

# Problem
# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

# Solution
# Time O(n) and space O(n)
# We use dfs to insert a node into a binary tree. We leverage the Binary Tree property to make decisions on insertion.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

from problems.trees.bfs.BinaryTree import TreeNode


def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)
    return root


# --- or ---

def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
        return TreeNode(val)

    def dfs(node):
        if val < node.val:
            if node.left:
                dfs(node.left)
            else:
                node.left = TreeNode(val)
                return
        else:
            if node.right:
                dfs(node.right)
            else:
                node.right = TreeNode(val)
                return

    dfs(root)
    return root
