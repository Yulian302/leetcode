# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
# Difficulty: Medium
# Tags: tree n-ary levelorder_traversla levelorder bfs

# Problem
# Given an n-ary tree, return the level order traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

# Solution
# Time O(N) and space O(N).

# We can simply use iterative BFS approach to simulate a level-order traversal for N-ary Tree. We can use Queue for that purpose.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

from collections import deque
from typing import List


def levelOrder(root: "Node") -> List[List[int]]:  # type: ignore
    if not root:
        return []
    q = deque([root])
    res = []
    while q:
        nNodes = len(q)
        level_nodes = []
        for _ in range(nNodes):
            node = q.popleft()
            level_nodes.append(node.val)
            for child in node.children:
                q.append(child)
        res.append(level_nodes)
    return res
