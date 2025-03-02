# https://leetcode.com/problems/binary-tree-right-side-view/
# Difficulty: Medium
# Tags: tree binary_tree bfs

# Problem
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Solution
# Time O(n) and space O(n) as we still move across all nodes, not just levels
# We use bfs to move across the levels of our tree and add the last node in a queue to our answer array. This approach gives us the right side view of a tree.
from collections import deque
from typing import Optional

from problems.trees.bfs.BinaryTree import TreeNode


def rightSideView(root: Optional[TreeNode]):
    if not root:
        return []
    ans = []
    q = deque([root])
    while q:
        n_nodes = len(q)
        ans.append(q[-1].val)
        for _ in range(n_nodes):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return ans
