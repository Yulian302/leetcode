# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
# Difficulty: Medium
# Tags: tree binary_tree ancestor dfs

# Problem
# Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

# Solution
# Time O(n) and space O(n)
# We use dfs to keep move down the tree from a root to the leaf and keep track of a max and min values. Then we return the difference of these values. For solving a problem we find the maximum difference for left and right subtrees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root) -> int:

        def dfs(node, min_val, max_val):
            if not node:
                return max_val - min_val

            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)

            return max(
                dfs(node.left, min_val, max_val), dfs(
                    node.right, min_val, max_val)
            )

        return dfs(root, root.val, root.val)
