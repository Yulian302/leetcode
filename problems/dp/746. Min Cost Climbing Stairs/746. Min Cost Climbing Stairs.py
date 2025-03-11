# https://leetcode.com/problems/min-cost-climbing-stairs/
# Difficulty: Easy
# Tags: dp min

# Problem
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

# Solution
# Time O(n) and space O(n)

# Function dp(i) finds the min cost to climb step i -> `state: i of type int, dp returns a number.`

# In order to solve the whole problem, we can first solve it's subproblems and derive the solution from them.
# We can start from either step 0 or step 1, which means dp(0)=dp(1)=0 -> the min cost to climb stair 0 or stair 1 is 0 as we can simply start from either one.

# Then to find a min cost to climb step i, we can find the min cost to climb step i-1 and add cost i-1
# --- or ---
# find the min cost to climb step i-2 and add cost i-2
# Therefore, we find minimum from these options -> dp(i) = min(dp(i-1) + costs[i-1], dp(i-2) + costs[i-2])
# This recurrence derives from the description: `you can either climb one or two steps`

# For solving a dp, we use top-down (recursion with memoization) or bottom-up (iteratively fill up the dp array).
# The number of states for this problem is 1, so it's a 1D dp problem.

def minCostClimbStairsTopDown(costs):
    memo = {}

    def dp(i):
        if i <= 1:
            return 0

        if i in memo:
            return memo[i]

        memo[i] = min(dp(i-1)+costs[i-1], dp(i-2)+costs[i-2])
        return memo[i]

    return dp(len(costs))


def minCostClimbStairsBottomUp(costs):
    n = len(costs)
    dp = [None] * (n+1)
    dp[0] = 0
    dp[1] = 0
    for i in range(2, n+1):
        dp[i] = min(dp[i-1]+costs[i-1], dp[i-2]+costs[i-2])

    return dp[n]


print(minCostClimbStairsTopDown([10, 15, 20]))
print(minCostClimbStairsBottomUp([10, 15, 20]))
