# https://leetcode.com/problems/house-robber/
# Difficulty: Medium
# Tags: dp max 1D

# Problem
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Solution
# Time O(n) and space O(n)

# Function dp(i) finds the max money to rob houses till i -> `state: i of type int, dp returns a number.`

# In order to solve the whole problem, we can first solve it's subproblems and derive the solution from them.
# If we have only one house, the max money is that house money. If we have two houses, the max money is the max between these two houses as we are only allowed to rob one of them. Thus, dp(0)=nums[0], dp(1)=max(nums[0],nums[1])

# Then to get a max money to rob till house i, we can either get the max money robbing till house i-1 skipping current house or get the max money robbing till house i-2 and robbing this house. Thus, we have the following:
# dp(i) = max(dp(i-1), dp(i-2) + nums[i])
# This recurrence derives from the description: `we can't rob adjacent houses`

# For solving a dp, we use top-down (recursion with memoization) or bottom-up (iteratively fill up the dp array).
# The number of states for this problem is 1, so it's a 1D dp problem.

def robTopDown(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[1]

    memo = {}

    def dp(i):
        if i == 0:
            return nums[0]

        if i == 1:
            return max(nums[0], nums[1])

        if i in memo:
            return memo[i]

        memo[i] = max(dp(i-1), dp(i-2)+nums[i])
        return memo[i]

    return dp(len(nums)-1)


def robBottomUp(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    n = len(nums)
    dp = [None] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])

    return dp[n-1]


print(robTopDown([2, 7, 9, 3, 1]))
print(robBottomUp([2, 7, 9, 3, 1]))
