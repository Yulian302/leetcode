# https://leetcode.com/problems/top-k-frequent-elements/
# Difficulty: Medium
# Tags: heap min_heap topK

# Problem
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Solution
# Time O(NlogK) as we perform heapify (LogK) for N times and space O(N) as we create a heap using array
# We simply use max heap to store most frequent elements using their frequencies as comparable values for a heap. Then we perform pop operation K times to return most frequent values.


from collections import defaultdict
import heapq
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    if k == len(nums):
        return nums
    counter = defaultdict(int)
    for num in nums:
        counter[num] += 1

    max_heap = []
    for val, freq in counter.items():
        heapq.heappush(max_heap, (-freq, val))
    return [heapq.heappop(max_heap)[1] for _ in range(k)]
