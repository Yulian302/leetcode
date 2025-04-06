# https://leetcode.com/problems/n-ary-tree-postorder-traversal/
# Difficulty: Easy
# Tags: tree n-ary postorder_traversal postorder

# Problem
# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

# Solution
# Recursive: Time O(N) and space O(N).
# Iterative: Time O(N) as reversing in a loop takes AT MOST O(N) [amortized] and space O(N).
# The idea behind is same as for binary trees, but here we have children as a list of children instead of left and right children.


"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


from typing import List


def postorder(root: "Node") -> List[int]:  # type: ignore
    if not root:
        return []
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        for child in node.children:
            stack.append(child)

    res.reverse()
    return res


# --- or ---

# recursive
def postorder(root: 'Node') -> List[int]:  # type: ignore
    if not root:
        return []

    def helper(node):
        if not node:
            return

        for child in node.children:
            helper(child)

        res.append(node.val)

    res = []
    helper(root)
    return res
