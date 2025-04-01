# https://leetcode.com/problems/find-peak-element/
# Difficulty: Medium
# Tags: binary_search peak

# Problem
# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

# Solution
# O(log2(N)) time and space O(1)
# We use advance binary search algorithm to solve this problem. If the mid element is less than the right element (local minimum), then we move to the right, otherwise we move to the left. Termination is handled when left==right, namely when we stay at peak itself.


from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid
        return left
