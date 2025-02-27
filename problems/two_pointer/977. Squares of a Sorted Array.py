# Difficulty: Easy
# Tags: two_pointers sorted_array

# Problem
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Solution
# Time O(n) and space O(n)
# We use two pointers technique in this situation as in our non-decreasing array we have to compare absolute values of our elements and append the square of it to the end of resulting array.

from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    n = len(nums)
    low, high = 0, n - 1
    res = [0] * n
    idx = n - 1
    while low <= high:
        low_num = nums[low]
        high_num = nums[high]
        if abs(low_num) > abs(high_num):
            res[idx] = low_num * low_num
            low += 1
        else:
            res[idx] = high_num * high_num
            high -= 1
        idx -= 1
    return res
