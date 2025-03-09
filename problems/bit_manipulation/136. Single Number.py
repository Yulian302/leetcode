# https://leetcode.com/problems/single-number/
# Difficulty: Easy
# Tags: unique bitwise xor

# Problem
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Solution
# Time O(n) and space O(1)
# In order to find single element, we can use XOR operator. First we init the res variable to 0.
# 0 ^ a = a
# a ^ a = 0
# Thus, we can use this property to find a single element in the array.

from typing import List


def singleNumber(nums: List[int]) -> int:
    single = 0
    for num in nums:
        single ^= num
    return single
