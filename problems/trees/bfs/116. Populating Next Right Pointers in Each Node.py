# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# Difficulty: Medium
# Tags: tree binary_tree bfs

# Problem
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }

# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Solution
# Time O(n) and space O(n) for bfs using queue.
# We can use bfs to solve this problem (for non constant time solution). For each level in level-order traversal we connect nodes with next pointer one by one.

from collections import deque


def connect(root):
    if not root:
        return None

    q = deque([root])
    while q:
        curr = None
        for _ in range(len(q)):
            node = q.popleft()
            if curr:
                curr.next = node
            curr = node

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return root


# --- or ---
# Time O(N) and space O(1) for a recursive solution (if not counting a call stack).
# We use DFS. For a node that has children (left and right), create a pointer next from left to right child. For a node that has a pointer to the next pointer and has a right child, create a next pointer from its right child to next's left child.
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


def connect(root):
    if not root:
        return

    if root.left and root.right:
        root.left.next = root.right

    if root.next and root.right:
        root.right.next = root.next.left

    connect(root.left)
    connect(root.right)

    return root
