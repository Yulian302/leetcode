# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
# Difficulty: Medium
# Tags: sliding_window subarray

# Problem
# You are given an integer array nums and a positive integer k.

# Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

# A subarray is a contiguous sequence of elements within an array.

# Solution
# Time O(n) and space O(1)
# We use sliding window for this problem. After finding the max element (O(N)), we must create a correct window where number of max elements equals to `k`. Then we shrink the window up until this property is not violated and add left index to our answer. Adding left index at each iteration is a neat trick to find the number of subarrays where that property is not violated.


from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        left = 0
        ans = 0
        count = 0
        for right in range(len(nums)):
            if nums[right] == max_element:
                count += 1

            while count == k:
                if nums[left] == max_element:
                    count -= 1
                left += 1
            ans += left
        return ans
