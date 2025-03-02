# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Difficulty: Medium
# Tags: tree binary_tree bfs

# Problem
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# Solution
# Time O(n) and space O(n)
# I could come up with two options: we use bfs to move over levels of the binary tree. And:
#   1) We reverse the logic when adding to queue and popping from it when we need a right-to-left order.
#       --- or ---
#   2) We just reverse the elements in the queue when we need a right-to-left order.

from collections import deque
from typing import List, Optional

from problems.trees.bfs.BinaryTree import TreeNode


def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    ans = []
    left_to_right = True
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            if left_to_right:
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                node = q.pop()
                level.append(node.val)
                if node.right:
                    q.appendleft(node.right)
                if node.left:
                    q.appendleft(node.left)

        ans.append(level)
        left_to_right = not left_to_right
    return ans


# ---- or ----


def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    ans = []
    left_to_right = True
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level if left_to_right else level[::-1])
        left_to_right = not left_to_right
    return ans
