# https://leetcode.com/problems/clone-graph/
# Difficulty: Medium
# Tags: graph clone

# Problem
# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }


# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

# Solution
# Time O(V+E) and space O(V)
# We can use bfs to traverse the nodes of a graph while updating references and neighbors in a clone map declared earlier.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
from typing import Optional
from xml.dom import Node


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:

        if not node:
            return None

        cloneMap = {node: Node(node.val)}

        q = deque([node])
        while q:
            n = q.popleft()

            for nei in n.neighbors:
                if nei not in cloneMap:
                    cloneMap[nei] = Node(nei.val)
                    q.append(nei)

                cloneMap[n].neighbors.append(cloneMap[nei])
        return cloneMap[node]
