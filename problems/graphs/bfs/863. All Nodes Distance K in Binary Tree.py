# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# Difficulty: Medium
# Tags: graph binary_tree bfs

# Problem
# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

# You can return the answer in any order.

# Solution
# Time O(n) and space O(n)
# In an ordinary binary tree we cannot access parent nodes, so it will be very hard to start from target node and continue to remaining nodes. The solution is - to add parent pointer for each node recursively. Then we can use bfs implemented iteratively to visit other nodes, update distance and append corresponding nodes with distance k to our resulting array.

from collections import deque
from typing import List

from problems.trees.bfs.BinaryTree import TreeNode


def distanceK(root: TreeNode, target: TreeNode, k: int) -> List[int]:

    def add_parent(cur, parent):
        if cur:
            cur.parent = parent
            add_parent(cur.left, cur)
            add_parent(cur.right, cur)

    add_parent(root, None)
    ans = []

    q = deque([(target, 0)])
    seen = set([target])
    while q:
        n = len(q)
        for _ in range(n):
            node, curr_dist = q.popleft()
            if curr_dist == k:
                ans.append(node.val)
            if node.left and node.left not in seen:
                seen.add(node.left)
                q.append((node.left, curr_dist + 1))
            if node.right and node.right not in seen:
                seen.add(node.right)
                q.append((node.right, curr_dist + 1))
            if node.parent and node.parent not in seen:
                seen.add(node.parent)
                q.append((node.parent, curr_dist + 1))

    return ans
