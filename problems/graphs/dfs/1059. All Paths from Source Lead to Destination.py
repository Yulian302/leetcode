# https://leetcode.com/problems/all-paths-from-source-lead-to-destination/
# Difficulty: Medium
# Tags: graph dfs cycle

# Problem
# Given the edges of a directed graph where edges[i] = [ai, bi] indicates there is an edge between nodes ai and bi, and two nodes source and destination of this graph, determine whether or not all paths starting from source eventually, end at destination, that is:

#     At least one path exists from the source node to the destination node
#     If a path exists from the source node to a node with no outgoing edges, then that node is equal to destination.
#     The number of possible paths from source to destination is a finite number.

# Return true if and only if all roads from source lead to destination.

# Solution
# Time O(V+E) and space O(V)
# This is quite a hard problem, because the graph may contain cycles and parallel connections. DFS can be used to solve it. Though we need to use memoization to avoid TLE as the number of nodes can be up to 10^4. Each memo[i] is True or False, meaning `if node i leads to destination`. If we reached a destination node, we mark it as a success only if it has no outgoing edges. If we reach the dead end, we check whether it's a destination node. When new node is in visited set, it means we have a cycle and we return False. So, we have a lot of edge cases and constraints for this problem. And the function returns true only if none of them is violated.

from collections import defaultdict
from typing import List


class Solution:
    def leadsToDestination(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = defaultdict(list)
        # directed graph
        for x, y in edges:
            graph[x].append(y)

        memo = {}

        def dfs(node, seen):

            if node in memo:
                return memo[node]

            if node in seen:
                memo[node] = False
                return

            # reach
            if node == destination:
                memo[node] = not graph[node]
                return memo[node]

            if not graph[node]:
                memo[node] = False
                return False

            seen.add(node)
            # explore
            for nei in graph[node]:
                if not dfs(nei, seen):
                    memo[nei] = False
                    seen.remove(node)
                    return False

            seen.remove(node)

            memo[node] = True
            return True

        return dfs(source, set())
