# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
# Difficulty: Hard
# Tags: dp max 1D interval nonoverlapping

# Problem
# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

# You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

# If you choose a job that ends at time X you will be able to start another job that starts at time X.


# Solution
# Time O(NlogN) and space O(N)

# Function dp(i) finds the max profit for doing jobs up to i time -> `state: i of type int, dp returns a number.`

# In order to solve the whole problem, we can first solve it's subproblems and derive the solution from them.
# We have to find the maximum value of non overlapping intervals. Intervals must not be strictly less than -> one job can be started as soon as another job is finished.

# So first we have to sort the jobs by their end time. Then we define our dp recurrence relation the following way: dp[i+1] = max(dp[i], gold + dp[j]), where j is the index of non overlapping interval for current interval.
# This recurrence means: the maximum profit for jobs up to i time is the maximum of last best profit up to i-1 time or current profit plus the one which is non overlapping. dp[0] = 0 -> if we have no jobs, we can't get profit. Binary search efficiently finds the right most insertion index of an element, which helps us find the end time of a last non overlapping interval. (for not strict non overlapping start is passed)!


# For solving a dp, we use top-down (recursion with memoization) or bottom-up (iteratively fill up the dp array).
# The number of states for this problem is 1, so it's a 1D dp problem.

from bisect import bisect_right
from typing import List


def jobScheduling(
    startTime: List[int], endTime: List[int], profit: List[int]
) -> int:
    jobsTimes = list(zip(startTime, endTime, profit))
    jobsTimes.sort(key=lambda x: x[1])
    endTimes = [jobTime[1] for jobTime in jobsTimes]

    dp = [0] * (len(jobsTimes) + 1)

    for i in range(len(jobsTimes)):
        start, end, profit = jobsTimes[i]
        j = bisect_right(endTimes, start)
        dp[i + 1] = max(dp[i], profit + dp[j])
    return dp[-1]
