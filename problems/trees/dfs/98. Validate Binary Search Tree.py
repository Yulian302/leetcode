# https://leetcode.com/problems/validate-binary-search-tree/
# Difficulty: Medium
# Tags: tree bst dfs

# Problem
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

#     The left

#     of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.


# Solution
# Time O(n) and space O(n)
# We use inorder traversal in order to traverse BST nodes in ascending order and meanwhile keeping track of the curr element. If new element is less than a previous element, it is not a BST. I implemented a DFS iteratively using a stack.

from cmath import inf
from typing import Optional

from problems.trees.bfs.BinaryTree import TreeNode


def isValidBST(root: Optional[TreeNode]) -> bool:
    curr = root
    stack = []
    prev = -inf
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            if curr.val <= prev:
                return False
            prev = curr.val
            curr = curr.right
    return True
