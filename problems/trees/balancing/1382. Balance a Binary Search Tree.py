# https://leetcode.com/problems/balance-a-binary-search-tree/
# Difficulty: Medium
# Tags: tree binary_tree balance

# Problem
# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.


# Solution
# Time O(n) for inorder traversal and O(logN) for rebuilding = O(N) in total; and space O(n)
# AVL self-balancing BST algorithm is an overhead for this problem. (What a pity)! We have to simply traverse the tree inorder to get the nodes in ascending order. Then we can use binary search approach to recursively recreate a BST.

from typing import Optional
from problems.trees.bfs.BinaryTree import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder_traversal(node):
            if not node:
                return []

            return (
                inorder_traversal(node.left)
                + [node.val]
                + inorder_traversal(node.right)
            )

        def build_balanced(nums, left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = build_balanced(nums, left, mid - 1)
            node.right = build_balanced(nums, mid + 1, right)
            return node

        nums = inorder_traversal(root)
        return build_balanced(nums, 0, len(nums) - 1)
