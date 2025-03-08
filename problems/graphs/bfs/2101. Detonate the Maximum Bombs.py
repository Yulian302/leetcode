# https://leetcode.com/problems/detonate-the-maximum-bombs/
# Difficulty: Medium
# Tags: graph bfs

# Problem
# You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

# The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

# You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

# Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

# Solution
# Time O(n^2) and space O(n^2)
# We can convert this problem into a graph, where node A is connected to node B if A can detonate node B when it explodes. Then we can use bfs to check the number of connected nodes (maximum detonations from explosion) if exploding starting node. Thus, we need to find maximum of called bfs functions.

from collections import defaultdict, deque
from typing import List


def maximumDetonation(bombs: List[List[int]]) -> int:
    n = len(bombs)

    def will_detonate(b1, b2):
        x1, y1, r1 = bombs[b1]
        x2, y2, _ = bombs[b2]
        return (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r1**2

    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i != j and will_detonate(i, j):
                graph[i].append(j)

    def bfs(start):
        q = deque([start])
        seen = {start}
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    q.append(neighbor)
        return len(seen)

    return max(bfs(i) for i in range(n))
