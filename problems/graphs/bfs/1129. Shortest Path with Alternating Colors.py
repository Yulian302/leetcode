# https://leetcode.com/problems/shortest-path-with-alternating-colors/
# Difficulty: Medium
# Tags: graph bfs

# Problem
# You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

# You are given two arrays redEdges and blueEdges where:

#     redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
#     blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.

# Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

# Solution
# Time O(n) and space O(n)
# We use bfs and start from node 0 to other nodes while checking for color change and counting steps taken. Then when we reach a corresponding node we append found number of steps to answer array. We have to keep track of visited nodes using node number and last color to find all possible solutions for the shortest path.

from collections import defaultdict, deque
from typing import List


def shortestAlternatingPaths(
    n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
) -> List[int]:
    graph = defaultdict(list)
    for x, y in redEdges:
        graph[x].append([y, 0])
    for x, y in blueEdges:
        graph[x].append([y, 1])

    answer = [-1] * n
    answer[0] = 0
    # (node, steps, last_edge_color)
    q = deque([(0, 0, -1)])
    # (node, last_edge_color)
    seen = {(0, -1)}
    while q:
        for _ in range(len(q)):
            node, steps, last_color = q.popleft()
            for nei, color in graph[node]:
                if (nei, color) not in seen and color != last_color:
                    seen.add((nei, color))
                    q.append((nei, steps + 1, color))
                    if answer[nei] == -1:
                        answer[nei] = steps + 1
    return answer
