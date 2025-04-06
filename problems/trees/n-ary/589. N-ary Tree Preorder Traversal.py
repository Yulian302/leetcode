# https://leetcode.com/problems/n-ary-tree-preorder-traversal/
# Difficulty: Easy
# Tags: tree n-ary preorder_traversal preorder

# Problem
# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

# Solution
# Recursive: Time O(N) and space O(N).
# Iterative: Time O(N) and space O(N) worst when tree is imbalanced.
# The idea behind is same as for binary trees, but here we have children as a list of children instead of left and right children. For iterative approach, stack pushing must be reversed to maintain natural order of tree nodes in preorder traversal.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


from typing import List


def preorder(root: "Node") -> List[int]:  # type: ignore
    if root is None:
        return []

    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        stack.extend(node.children[::-1])
    return res


# --- or ---

# recursive

def preorder(root: 'Node') -> List[int]:  # type: ignore
    res = []

    def helper(node):
        if not node:
            return

        res.append(node.val)
        for child in node.children:
            helper(child)

    helper(root)
    return res
