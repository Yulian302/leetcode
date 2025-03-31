# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Difficulty: Medium
# Tags: binary_search pivot rotated

# Problem
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Solution
# O(logN) time and space O(1)
# As the array is rotated, we must find a pivot index - the index at which array is becoming rotated. To do this, we can use binary search with some modification. If middle element is more than right-most array element, we move to the right, otherwise we move to the left. Thus, at the end `left-1` will be the pivot index. Then we can simply use binary search for both subarray divided by pivot index to find a target. Overall time complexity is O(3*logN) which is eventually O(logN). Space is constant as we do comparison just in-place.

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        # find pivot index
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        def binarySearch(left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        ans = binarySearch(0, left - 1, target)
        if ans != -1:
            return ans
        return binarySearch(left, n - 1, target)
