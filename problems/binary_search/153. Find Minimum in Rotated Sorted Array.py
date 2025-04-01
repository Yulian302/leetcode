# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Difficulty: Medium
# Tags: binary_search rotated

# Problem
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

#     [4,5,6,7,0,1,2] if it was rotated 4 times.
#     [0,1,2,4,5,6,7] if it was rotated 7 times.

# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Solution
# O(log2(N)) time and space O(1)
# In order to find the minimum element in a rotated array we have to find a pivot index (the index of rotation). We can efficiently use binary search for that purpose. We use left==right termination as we need to find a single element in an array of unique elements. If mid element is more than right-most element in array, then we should move right -> to the pivot. Otherwise, we should move left. In the end, left and right will be the pivot index, so the minimum element will be array[left] or array[right].

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
