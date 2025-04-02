# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/
# Difficulty: Medium
# Tags: greedy triplets maximum

# Problem
# You are given a 0-indexed integer array nums.

# Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

# The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].

# Solution
# Time O(n) and space O(n)
# We can use a greedy approach to solve this problem. The thing is, we have to maximize nums[i] in the range [0,j) and maximize nums[k] in the range [j+1, n), thus we can create two max prefix arrays to represent max values from the left and from the right. Then we iterate over potential nums[j], j = [1,n-1] and update the maximum found triplet of indices using max prefixes for left and right.

from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)

        left_max = [0] * n
        right_max = [0] * n

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i - 1])
            right_max[n - 1 - i] = max(right_max[n - i], nums[n - i])
        res = 0

        for j in range(1, n - 1):
            res = max(res, (left_max[j] - nums[j]) * right_max[j])

        return res
