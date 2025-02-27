# Difficulty: Medium
# Tags: sliding_window product subarray

# Problem
# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

# Solution
# Time O(n) and space O(1)
# We use sliding window technique to slide over the array and find a window with product less than k while updating the number of found subarrays. Number of subarrays is: (right-left+1) -> same as a length of a window.

from typing import List


def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0
    left = 0
    prod = 1
    ans = 0
    for right in range(len(nums)):
        prod *= nums[right]
        while prod >= k:
            prod //= nums[left]
            left += 1
        ans += right - left + 1
    return ans
