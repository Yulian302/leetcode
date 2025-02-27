# Difficulty: Medium
# Tags: two_pointers sorted_array sum

# Problem
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

# Solution
# Time O(n) and space O(1)
# We use two pointers technique to check the sum of low and high elements. If the sum is more than target, we move high to the left (as the array is sorted in asc order), if it's less than target, we move the low to the right. If it's equal to the sum, we just return incremented indexes for low and right, as our array is 1-indexed.
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers)-1
        while low < high:
            curr_sum = numbers[low]+numbers[high]
            if curr_sum < target:
                low += 1
            elif curr_sum > target:
                high -= 1
            else:
                return [low+1, high+1]
