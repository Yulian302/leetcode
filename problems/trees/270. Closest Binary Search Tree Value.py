
# https://leetcode.com/problems/closest-binary-search-tree-value/
# Difficulty: Easy(premium)
# Tags: tree bst

# Problem
# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.

# Solution
# Time O(logn) as we traverse over a BST and space O(1) as we work only on pointers without auxiliary space
# We use a while loop and BST property to move over nodes where target can be. At first we suppose closest node is the root node. Then we update closest node if the absolute difference is smaller. If it's same for both nodes, we choose the smaller one.

from typing import Optional

from problems.trees.bfs.BinaryTree import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def closestValue(root: Optional[TreeNode], target: float) -> int:
    closest = root.val
    while root:
        if abs(root.val - target) < abs(closest - target):
            closest = root.val
        elif abs(root.val - target) == abs(closest - target):
            closest = min(closest, root.val)
        if target < root.val:
            root = root.left
        else:
            root = root.right
    return closest
