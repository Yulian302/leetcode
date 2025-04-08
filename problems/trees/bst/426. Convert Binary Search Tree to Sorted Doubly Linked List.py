# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
# Difficulty: Medium
# Tags: tree binary_tree bst dll

# Problem
# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

# You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

# We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

# Solution
# Time O(n) and space O(n)
# We can traverse the BST inorder to get it's nodes in a sorted order. Then we define a dummy node and prev node pointer and go through existing tree while constructing a doubly linked list using left and right node pointers. In the end we have to close the cycle.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


from xml.dom import Node


class Solution:
    def treeToDoublyList(self, root):
        # inorder traversal for sorted elements
        if not root:
            return
        dummy = Node(0)
        self.prev = dummy

        def inorder_traverse(node):
            if not node:
                return

            inorder_traverse(node.left)

            self.prev.right = node
            node.left = self.prev
            self.prev = node

            inorder_traverse(node.right)

        inorder_traverse(root)
        head = dummy.right
        self.prev.right = head
        head.left = self.prev
        return head
