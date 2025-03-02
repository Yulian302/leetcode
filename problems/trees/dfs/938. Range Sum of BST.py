# https://leetcode.com/problems/range-sum-of-bst/
# Difficulty: Easy
# Tags: tree bst dfs

# Problem
# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# Solution
# Time O(n) and space O(n)
# We use dfs to traverse the tree and include only values within the range. In order to optimize solution, we prune unusefull subtrees leveraging BST property.


from typing import Optional

from problems.trees.bfs.BinaryTree import TreeNode


def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
    curr_sum = 0

    def dfs(node):
        nonlocal curr_sum
        if node is None:
            return
        if low <= node.val <= high:
            curr_sum += node.val
        if node.val > low:
            dfs(node.left)
        if node.val < high:
            dfs(node.right)

    dfs(root)
    return curr_sum
