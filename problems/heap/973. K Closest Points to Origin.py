# https://leetcode.com/problems/k-closest-points-to-origin/
# Difficulty: Medium
# Tags: heap max_heap closest

# Problem
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Solution
# Time O(NlogK): heapify takes only O(logK) time as we keep our heap at most size K; and space O(N).
# To keep K closet (or K elements with smallest distance) we should use max heap. (smallest -> max heap, largest -> min heap)!!! And we keep the size of the heap at maximum K elements. Thus the resulting heap itself is K closest points to (0,0).

import heapq
from math import sqrt
from typing import List


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    max_heap = []
    for x, y in points:
        # euclidian distance of a point to the center of coordinates: sqrt(x^2+y^2)
        heapq.heappush(max_heap, (-sqrt(x * x + y * y), [x, y]))
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return [heapq.heappop(max_heap)[1] for _ in range(k)]
