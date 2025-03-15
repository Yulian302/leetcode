# https://leetcode.com/problems/maximum-earnings-from-taxi/
# Difficulty: Medium
# Tags: dp max 1D interval nonoverlapping

# Problem
# There are n points on a road you are driving your taxi on. The n points on the road are labeled from 1 to n in the direction you are going, and you want to drive from point 1 to point n to make money by picking up passengers. You cannot change the direction of the taxi.

# The passengers are represented by a 0-indexed 2D integer array rides, where rides[i] = [starti, endi, tipi] denotes the ith passenger requesting a ride from point starti to point endi who is willing to give a tipi dollar tip.

# For each passenger i you pick up, you earn endi - starti + tipi dollars. You may only drive at most one passenger at a time.

# Given n and rides, return the maximum number of dollars you can earn by picking up the passengers optimally.

# Note: You may drop off a passenger and pick up a different passenger at the same point.

# Solution
# Time O(NlogN) and space O(N)

# Function dp(i) finds the max profit for driving up to i given rides -> `state: i of type int, dp returns a number.`

# In order to solve the whole problem, we can first solve it's subproblems and derive the solution from them.
# We have to find the maximum value of non overlapping intervals. Intervals must be less than or equal (not strict) -> one passanger can be picked up at another passanger drop off time.

# So first we have to sort the rides by their end time. Then we define our dp recurrence relation the following way: dp[i+1] = max(dp[i], gold + dp[j]), where j is the index of non overlapping interval for current interval.
# This recurrence means: the maximum rides profit for i given rides is the maximum of previous best profit or current ride profit plus previous non overlapping ride. dp[0] = 0 -> if we have no passangers, we can't get profit. Binary search efficiently finds the right most insertion index of an element, which helps us find the end time of a last non overlapping interval. (for not strict non overlapping start is passed)!


# For solving a dp, we use top-down (recursion with memoization) or bottom-up (iteratively fill up the dp array).
# The number of states for this problem is 1, so it's a 1D dp problem.

from bisect import bisect_right
from typing import List


def maxTaxiEarnings(n: int, rides: List[List[int]]) -> int:
    rides.sort(key=lambda x: x[1])
    end_points = [ride[1] for ride in rides]
    dp = [0] * (len(rides) + 1)

    for i in range(len(rides)):
        start, end, tip = rides[i]
        j = bisect_right(end_points, start)
        dp[i + 1] = max(dp[i], (end - start + tip) + dp[j])

    return dp[-1]
