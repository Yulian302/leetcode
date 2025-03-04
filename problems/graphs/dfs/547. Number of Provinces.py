# https://leetcode.com/problems/number-of-provinces/
# Difficulty: Medium
# Tags: graph dfs

# Problem
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.


# Solution
# Time O(N^2): for graph initialization and space O(N^2).
# We create our graph using a dictinary with node as key and list of connected nodes as value. Then we keep track of seen nodes to avoid infinite cycle. We iterate over nodes and update the answer if it is not seen. Then we use dfs for current node to eliminate other nodes that form a province (by adding to seen).

from collections import defaultdict
from typing import List


def findCircleNum(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)

    def dfs(node, seen):
        for nei in graph[node]:
            if nei not in seen:
                seen.add(nei)
                dfs(nei, seen)

    seen = set()
    ans = 0
    for i in range(n):
        if i not in seen:
            seen.add(i)
            ans += 1
            dfs(i, seen)
    return ans
