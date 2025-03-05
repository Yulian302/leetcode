# https://leetcode.com/problems/reachable-nodes-with-restrictions/
# Difficulty: Medium
# Tags: graph bfs dfs

# Problem
# There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

# You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.

# Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.

# Note that node 0 will not be a restricted node.

# Solution
# Time O(n) and space O(n)
# We use iterative bfs to move over the nodes (traverse the tree) and count only those nodes that are not restricted. We also did some kind of preprocessing: converted a list "restricted" into a set, as the number of nodes may be very big and searching in a list takes O(n) time meanwhile searching in a set - constant time O(1).

from collections import defaultdict, deque
from typing import List


def reachableNodes(
    n: int, edges: List[List[int]], restricted: List[int]
) -> int:

    restricted = set(restricted)
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    q = deque([0])
    ans = 0
    seen = {0}
    while q:
        n_nodes = len(q)
        for _ in range(n_nodes):
            node = q.popleft()
            ans += 1
            for nei in graph[node]:
                if nei not in restricted and nei not in seen:
                    q.append(nei)
                    seen.add(nei)
    return ans
