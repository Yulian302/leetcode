# https://leetcode.com/problems/balanced-binary-tree/
# Difficulty: Easy
# Tags: tree binary_tree balance

# Problem
# Given a binary tree, determine if it is height-balanced.

# Solution
# Time O(NlogN) or O(N^2) without early stop. Space O(N)
# Binary Tree is height balanced if the diff between it's left subtree height and right subtree height is not more than 1. In order to find if an entire binary tree is balanced we have to recursively call that check for each subtree rooted at node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from problems.trees.bfs.BinaryTree import TreeNode


class Solution:
    def getHeight(self, node):
        if not node:
            return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        return 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return (
            abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )
