# https://leetcode.com/problems/maximum-subarray/
# Difficulty: Medium
# Tags: kadane subarray maximum

# Problem
# Given an integer array nums, find the with the largest sum, and return its sum.

# Solution
# Time O(N) and space O(1)
# We can use Kadane's algorithm to find the maximum subarray sum. In simple terms, we iterate over the array updating current sum and setting it to 0 whenever it becomes negative. Thus we get rid of subarray of negative sum, which will never be the maximum. And still we have to update the maximum subarray sum at each step, because each potential current sum may be a maximum.

from typing import List


def maxSubArray(nums: List[int]) -> int:
    # kadane's algrorithm
    maxSub = nums[0]
    currSum = nums[0]
    for i in range(1, len(nums)):
        currSum = max(nums[i], currSum + nums[i])
        maxSub = max(maxSub, currSum)
    return maxSub

# --- or ---


def maxSubArray(nums: List[int]) -> int:
    # kadane's algrorithm
    maxSub = nums[0]
    currSum = nums[0]
    for i in range(1, len(nums)):
        if currSum < 0:
            currSum = 0
        currSum += nums[i]
        maxSub = max(maxSub, currSum)
    return maxSub
