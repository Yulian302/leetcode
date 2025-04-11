# https://leetcode.com/problems/delete-node-in-a-bst/
# Difficulty: Medium
# Tags: tree binary_tree delete_node bst

# Problem
# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

#     Search for a node to remove.
#     If the node is found, delete the node.


# Solution
# Time O(n) and space O(1)
# Node deletion in a BST is a bit more complex. We have a couple of edge cases. 1) If only left child exist -> return left child (substitute current with left child). 2) If only right child exist -> return right child. 3) If both exist, we need to find the successor (left-most child of a right child). Then we set successor's value to node value and recursively delete the successor's node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from problems.trees.bfs.BinaryTree import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                successor = root.right
                while successor.left:
                    successor = successor.left
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)

        return root
