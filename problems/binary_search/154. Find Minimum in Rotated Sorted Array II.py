# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
# Difficulty: Hard
# Tags: binary_search rotated

# Problem
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

#     [4,5,6,7,0,1,4] if it was rotated 4 times.
#     [0,1,4,4,5,6,7] if it was rotated 7 times.

# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

# You must decrease the overall operation steps as much as possible.

# Solution
# Time O(log2(N)) and space O(1)
# We use binary search to find the minimum number in rotated array (pivot element in our case). We have the following cases for current middle element: 1) Right-most number is less than mid -> move to the right. 2) Right-most number is more than mid -> move to the left. 3) Mid is same as right-most number -> decrement right pointer.

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1

        return nums[left]
