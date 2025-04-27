# https://leetcode.com/problems/find-greatest-common-divisor-of-array/
# Difficulty: Easy
# Tags: gcd array

# Problem
# Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

# Solution
# Time O(n) and space O(1)
# We use an euclidian algorithm to find the greatest common divisor of two numbers.


from math import inf
from typing import List


def findGCD(nums: List[int]) -> int:
    min_num = inf
    max_num = -inf

    for num in nums:
        min_num = min(min_num, num)
        max_num = max(max_num, num)

    while min_num:
        max_num, min_num = min_num, max_num % min_num

    return max_num
