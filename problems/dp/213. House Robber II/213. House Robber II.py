# https://leetcode.com/problems/house-robber-ii/
# Difficulty: Medium
# Tags: dp max 1D

# Problem
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Solution
# Time O(n) and space O(n)

# Function dp(i) finds the max money to rob houses till i -> `state: i of type int, dp returns a number.`

# In order to solve the whole problem, we can first solve it's subproblems and derive the solution from them.
# We can't rob adjacent houses and first and last houses are also adjacent as we have a cycle.

# Then to get a max money to rob till house i, we can either get the max money robbing till house i-1 skipping current house or get the max money robbing till house i-2 and robbing this house. Thus, we have the following:
# dp(i) = max(dp(i-1), dp(i-2) + nums[i])
# This recurrence derives from the description: `we can't rob adjacent houses`
# In order to solve this problem, we should find max money to rob houses skipping first and including last: nums[1:] and skipping last and including first: nums[:-1]
# So, we should get max of these subproblems -> max(robSimple(nums[1:]),robSimple(nums[:-1]))


# For solving a dp, we use top-down (recursion with memoization) or bottom-up (iteratively fill up the dp array).
# The number of states for this problem is 1, so it's a 1D dp problem.

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.robSimple(nums[:-1]), self.robSimple(nums[1:]))

    def robSimple(self, nums):
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        memo = {}

        def dp(i):
            if i < 0:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(dp(i - 2) + nums[i], dp(i - 1))
            return memo[i]

        return dp(len(nums) - 1)
