# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Difficulty: Easy (medium)
# Tags: heap min_heap k largest

# Problem
# You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

# You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

# Implement the KthLargest class:

#     KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
#     int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.


# Solution
# Time O(logK) for add; O(logN) for initialization; space O(K) for initialization and O(1) for add.
# We use min heap and maintain it in size K to have Kth largest score as a first (root) element in a heap.

import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums  # min heap
        heapq.heapify(self.min_heap)
        self.k = k

        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
