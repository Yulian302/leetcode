# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
# Difficulty: Easy
# Tags: tree n-ary dfs

# Problem
# Given a n-ary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

# Solution
# Time O(N) and space O(N).
# We can use different approaches for this problem. I've chosen an iterative DFS using stack. We populate the stack with node and current depth. One possible bug here which is really important is what is the value of self.children when node has no children? Is it None or empty list []?! That must be clarrified with an interviewer to avoid `for child in None`, what will crash the program.


"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(root: 'Node') -> int:  # type: ignore
        if not root:
            return 0
        # (node, depth)
        max_depth = 1
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            for child in node.children:
                stack.append((child, depth+1))
        return max_depth
