# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/
# Difficulty: Hard (Medium)
# Tags: sliding_window product

# Problem
# The score of an array is defined as the product of its sum and its length.

#     For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.

# Given a positive integer array nums and an integer k, return the number of non-empty subarrays of nums whose score is strictly less than k.

# A subarray is a contiguous sequence of elements within an array.

# Solution
# Time O(n) and space O(1)
# We use sliding window for this problem. To count the number of subarray for a valid window, we just add (right-left+1) to the counter.

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        curr_sum = 0
        count = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while left <= right and (right - left + 1) * curr_sum >= k:
                curr_sum -= nums[left]
                left += 1

            count += right - left + 1
        return count
