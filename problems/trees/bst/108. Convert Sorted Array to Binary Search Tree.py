# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Difficulty: Easy
# Tags: tree bst

# Problem
# Given an integer array nums where the elements are sorted in ascending order, convert it to a binary search tree.

# Solution
# Time O(N) and space O(N)
# We use the binary search idea to build a binary search tree from a sorted array. But we apply recursion to this logic.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from problems.trees.bfs.BinaryTree import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def build_tree(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = build_tree(left, mid - 1)
            node.right = build_tree(mid + 1, right)

            return node

        return build_tree(0, len(nums) - 1)
