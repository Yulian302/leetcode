# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Difficulty: Medium
# Tags: binary_search duplicates range

# Problem
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Solution
# O(log2(N)) time and space O(1)
# In order to find the range of target in a sorted array that contains duplicates, we can still use binary search but slightly differently. We can define a binary search for finding the left-most target index and right-most target index. Then if they both exist and inbounds, we return [left_bound, right_bound]. Otherwise we return [-1,-1]

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findLeftMost(nums, target):
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1

            return left

        def findRightMost(nums, target):
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return left - 1

        if not nums:
            return [-1, -1]

        left_bound = findLeftMost(nums, target)
        right_bound = findRightMost(nums, target)
        if (
            left_bound <= right_bound
            and right_bound < len(nums)
            and nums[left_bound] == target
            and nums[right_bound] == target
        ):
            return [left_bound, right_bound]
        else:
            return [-1, -1]
