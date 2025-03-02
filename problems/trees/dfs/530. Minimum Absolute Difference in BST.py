# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
# Difficulty: Easy
# Tags: tree bst dfs

# Problem
# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

# Solution
# Time O(n) and space O(n)
# In order to visit binary tree nodes in ascending order we can utilize inorder traversal. We can add visited nodes to the resulting array. Then we can simply iterate over our resulting array from 0 to n-1 and find a minimum difference between nodes: i+1 and i.

from cmath import inf
from typing import Optional

from problems.trees.bfs.BinaryTree import TreeNode


def getMinimumDifference(root: Optional[TreeNode]) -> int:
    values = []
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            values.append(curr.val)
            curr = curr.right
    curr_min = inf
    for i in range(len(values) - 1):
        curr_min = min(curr_min, values[i + 1] - values[i])
    return curr_min
