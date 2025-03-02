# https://leetcode.com/problems/deepest-leaves-sum/
# Difficulty: Medium
# Tags: tree binary_tree bfs

# Problem
# Given the root of a binary tree, return the sum of values of its deepest leaves.

# Solution
# Time O(n) and space O(n) for bfs using queue.
# We use bfs (breadth-first search) to traverse over each level of a binary tree and we update the curr sum of nodes for each level, thus at the end we will have a sum of deepest level nodes.

from collections import deque
from typing import Optional

from problems.trees.bfs.BinaryTree import TreeNode


def deepestLeavesSum(root: Optional[TreeNode]) -> int:
    q = deque([root])

    while q:
        n = len(q)
        curr_sum = 0
        for _ in range(n):
            node = q.popleft()
            curr_sum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return curr_sum
