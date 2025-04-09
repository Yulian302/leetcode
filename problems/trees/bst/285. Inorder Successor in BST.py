# https://leetcode.com/problems/inorder-successor-in-bst/
# Difficulty: Medium
# Tags: tree binary_tree bst inorder successor

# Problem
# Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

# The successor of a node p is the node with the smallest key greater than p.val.

# Solution
# Time O(n) and space O(n)
# We use inorder traversal to traverse the nodes in ascending order (as it is BST). When we reached the needed node, we set found to True and then at next node we visit we simply return that node's value. This simple trick is good for edge case where no successor node exist.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from typing import Optional
from problems.trees.bfs.BinaryTree import TreeNode


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        stack = []
        curr = root
        found = False

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if found:
                return curr

            if curr.val == p.val:
                found = True

            curr = curr.right
        return None
