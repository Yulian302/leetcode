# https://leetcode.com/problems/maximize-the-profit-as-the-salesman/
# Difficulty: Medium
# Tags: dp max 1D interval nonoverlapping

# Problem
# You are given an integer n representing the number of houses on a number line, numbered from 0 to n - 1.

# Additionally, you are given a 2D integer array offers where offers[i] = [starti, endi, goldi], indicating that ith buyer wants to buy all the houses from starti to endi for goldi amount of gold.

# As a salesman, your goal is to maximize your earnings by strategically selecting and selling houses to buyers.

# Return the maximum amount of gold you can earn.

# Note that different buyers can't buy the same house, and some houses may remain unsold.

# Solution
# Time O(NlogN) and space O(N)

# Function dp(i) finds the max profit for selling houses up to i given offers -> `state: i of type int, dp returns a number.`

# In order to solve the whole problem, we can first solve it's subproblems and derive the solution from them.
# We have to find the maximum value of non overlapping intervals. Intervals must be strictly less than -> one house cannot be sold twice.

# So first we have to sort the offers by their end time. Then we define our dp recurrence relation the following way: dp[i+1] = max(dp[i], gold + dp[j]), where j is the index of non overlapping interval for current interval.
# This recurrence means: the maximum gold for selling up to ith house is the maximum gold for selling up to previous house and current house plus maximum gold for last non overlapping house. dp[0] = 0 -> if we have no houses, we can't get gold. Binary search efficiently finds the right most insertion index of an element, which helps us find the end time of a last non overlapping interval. (for strict non overlapping start-1 is passed)!


# For solving a dp, we use top-down (recursion with memoization) or bottom-up (iteratively fill up the dp array).
# The number of states for this problem is 1, so it's a 1D dp problem.


from typing import List


def binary_search_right(arr, n):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if n < arr[mid]:
            high = mid
        else:
            low = mid + 1
    return low


def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
    offers.sort(key=lambda x: x[1])
    end_times = [offer[1] for offer in offers]
    dp = [0] * (len(offers) + 1)

    for i in range(len(offers)):
        start, end, gold = offers[i]
        j = self.binary_search_right(end_times, start - 1)
        dp[i + 1] = max(dp[i], gold + dp[j])

    return dp[-1]
