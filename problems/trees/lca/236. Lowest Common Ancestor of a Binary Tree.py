# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
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
# If there is only one deepest node, its LCA is itself. Otherwise, we have to use DFS to traverse the tree: if node is in one of the given nodes, we return itself. And if left node and right node exist for parent node, we return parent node (LCA). If only one exist (left or right), we return the one that exist (mainly because the LCA of a single node is itself).


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from problems.trees.bfs.BinaryTree import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root

        if left:
            return left

        return right
