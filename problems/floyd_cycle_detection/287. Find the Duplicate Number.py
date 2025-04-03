# https://leetcode.com/problems/find-the-duplicate-number/
# Difficulty: Medium
# Tags: duplicate cycle floyd

# Problem
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

# Solution
# Time O(n) and space O(1)
# As we know exactly the boundaries of array and its exact elements range, we can visualize it as a graph. The duplicate element in such array will form a cycle. And the cycle node is the duplicate number. We can use a Floyd's Cycle Detection technique using slow and fast pointers to find out if graph has a cycle as well as detect a node that creates it.

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast
