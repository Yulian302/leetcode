# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
# Difficulty: Medium
# Tags: graph

# Problem
# Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

# Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

# Notice that you can return the vertices in any order.

# Solution
# Time O(n) and space O(n)
# We need to find the nodes with no incoming edges.

from typing import List


def findSmallestSetOfVertices(n: int, edges: List[List[int]]) -> List[int]:
    with_incoming = [0] * n
    for _, to in edges:
        with_incoming[to] += 1
    return [i for i in range(n) if with_incoming[i] == 0]
