# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# Difficulty: Medium
# Tags: tree binary_tree bfs

# Problem
# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

# Solution
# Time O(n) and space O(n) for bfs using queue.
# We use bfs (breadth-first search) to traverse over each level of a binary tree and append the maximum node value to our resulting list.

from collections import deque
from cmath import inf


def largestValues(root):
    if not root:
        return []
    ans = []
    q = deque([root])
    while q:
        n = len(q)
        curr_max = -inf
        for _ in range(n):
            node = q.popleft()
            curr_max = max(curr_max, node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(curr_max)
    return ans
