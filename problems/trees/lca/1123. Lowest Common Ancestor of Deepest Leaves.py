# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
# Difficulty: Medium
# Tags: tree binary_tree bfs dfs lca

# Problem
# Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

# Recall that:

#     The node of a binary tree is a leaf if and only if it has no children
#     The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
#     The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.


# Solution
# Time O(N) and space O(N)
# We use bfs to find the deepest leaves. We can simply keep track of level_nodes and eventually the last level_nodes are the deepest nodes (leaves). Then we have to find the LCA of these nodes. If there is only one deepest node, its LCA is itself. Otherwise, we have to use DFS to traverse the tree: if node is in deepest nodes, we return itself. And if left node and right node exist for parent node, we return parent node (LCA). If only one exist (left or right), we return the one that exist (mainly because the LCA of a single node is itself).


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional

from problems.trees.bfs.BinaryTree import TreeNode


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deepest_nodes = []

        # find deepest nodes
        # O(N)
        q = deque([root])
        while q:
            nNodes = len(q)
            level_nodes = []
            for _ in range(nNodes):
                node = q.popleft()
                level_nodes.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        deepest_nodes = level_nodes

        # find lowest common ancestors
        if len(deepest_nodes) == 1:
            return deepest_nodes[0]
        # O(N)

        def find_lca(node):
            if not node or node in deepest_nodes:
                return node

            left = find_lca(node.left)
            right = find_lca(node.right)

            if left and right:
                return node

            if left:
                return left
            else:
                return right

        return find_lca(root)
