# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Difficulty: Easy
# Tags: hash_map intersection array

# Problem
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Solution
# Time O(n+m) and space O(min(n,m)) where m and n are sizes of array nums1, nums2 respectively.
# We use hash map to count the number of each num in second array. Then we simply iterate over another array and append those numbers that are in a hash map until they remain.

from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_count = Counter(nums2)
        res = []
        for num in nums1:
            if num in nums2_count and nums2_count[num] != 0:
                nums2_count[num] -= 1
                res.append(num)
        return res
