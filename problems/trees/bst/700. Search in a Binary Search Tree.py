# https://leetcode.com/problems/search-in-a-binary-search-tree/
# Difficulty: Easy
# Tags: tree binary_tree bst search

# Problem
# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

# Solution
# We can use a simple iterative method to perform a BST search without recursion. It will get us constant space complexity O(1) instead of O(N) because of recursive stack.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from problems.trees.bfs.BinaryTree import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
