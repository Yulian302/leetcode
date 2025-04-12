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
