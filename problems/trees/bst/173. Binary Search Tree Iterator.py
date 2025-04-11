# https://leetcode.com/problems/binary-search-tree-iterator/
# Difficulty: Medium
# Tags: tree binary_tree bst iterator

# Problem
# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

#     BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
#     boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
#     int next() Moves the pointer to the right, then returns the number at the pointer.

# Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

# You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

# Solution
# Time O(h) for init; O(1) for next(); O(1) for hasNext(); Space O(h).
# We leverage the inorder traversal iterative approach. While initializing we move to the left subtree leaf node, while adding nodes to the stack. If stack is not empty, next node exist. To get the next node, we pop from the stack and move to the right child left-most node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from problems.trees.bfs.BinaryTree import TreeNode


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        if not self.hasNext():
            return None

        node = self.stack.pop()
        if node.right:
            self._leftmost_inorder(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
