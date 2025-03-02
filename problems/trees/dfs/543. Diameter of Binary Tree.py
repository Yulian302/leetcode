# https://leetcode.com/problems/diameter-of-binary-tree/
# Difficulty: Easy(medium)
# Tags: tree binary_tree dfs

# Problem
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# Solution
# Time O(n) and space O(n)
# We use dfs approach to find the maximum depth of left and right subtrees. At each node, we update our maximum diameter as a sum of left and right subtrees depths. The resulting maximum diameter is the longest path between any two nodes in a tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def diameterOfBinaryTree(root) -> int:
    max_diameter = 0

    def dfs(node):
        nonlocal max_diameter
        if not node:
            return 0

        left_depth = dfs(node.left)
        right_depth = dfs(node.right)

        max_diameter = max(max_diameter, left_depth+right_depth)
        return 1 + max(left_depth, right_depth)

    dfs(root)
    return max_diameter
