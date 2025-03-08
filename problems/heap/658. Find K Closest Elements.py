# https://leetcode.com/problems/find-k-closest-elements/
# Difficulty: Medium
# Tags: heap top closest

# Problem
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

#     |a - x| < |b - x|, or
#     |a - x| == |b - x| and a < b

# Solution
# Time O((N+K)logK) and space O(N).
# We use min heap and add distances to it. Then we can find top K closest elements.


import heapq
from typing import List


def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    heap = []

    for num in arr:
        distance = abs(x - num)
        heapq.heappush(heap, (-distance, -num))
        if len(heap) > k:
            heapq.heappop(heap)

    return sorted([-pair[1] for pair in heap])


# --- or ---


def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    min_heap = []
    for num in arr:
        heapq.heappush(min_heap, (abs(x - num), num))
    return sorted([heapq.heappop(min_heap)[1] for _ in range(k)])
