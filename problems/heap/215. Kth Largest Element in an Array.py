# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Difficulty: Medium
# Tags: heap min_heap K largest

# Problem
# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?


# Solution
# Time O(nlogk) and space O(n)
# We can use min heap to find K largest element. If we want to have K largest on top of min heap, we just need to keep our heap same size as K during population.

from heapq import heappop, heappush
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    min_heap = []
    for num in nums:
        heappush(min_heap, num)
        if len(min_heap) > k:
            heappop(min_heap)
    return min_heap[0]
