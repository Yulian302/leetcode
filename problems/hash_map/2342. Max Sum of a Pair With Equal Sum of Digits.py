# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
# Difficulty: Medium
# Tags: array pairs

# Problem
# You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

# Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions. If no such pair of indices exists, return -1.

# Solution
# Time O(NlogN) due to sorting and space O(N).
# First we create a list of values (digit sum, number) and sort it. We get a list of pairs sorted in non-decreasing order where pairs with same digit sum are located near each other. Then we iterate over the list and update biggest sum of elements with equal digit sums.


from cmath import inf
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def getDigitsSum(num):
            curr = 0
            while num:
                curr += num % 10
                num //= 10
            return curr

        digit_sum_pairs = []
        for num in nums:
            digit_sum = getDigitsSum(num)
            digit_sum_pairs.append((digit_sum, num))

        digit_sum_pairs.sort()
        biggest = -inf
        for i in range(1, len(digit_sum_pairs)):
            curr_digit_sum = digit_sum_pairs[i][0]
            prev_digit_sum = digit_sum_pairs[i - 1][0]
            if curr_digit_sum == prev_digit_sum:
                biggest = max(
                    biggest, digit_sum_pairs[i - 1][1] + digit_sum_pairs[i][1]
                )

        return biggest if biggest != -inf else -1
        # (4,13) (7,43) (7,1) (9, 18) (9,36)
