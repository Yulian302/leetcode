# https://leetcode.com/problems/minimum-cost-to-connect-sticks/
# Difficulty: Medium
# Tags: heap min_heap minimum

# Problem
# You have some number of sticks with positive integer lengths. These lengths are given as an array sticks, where sticks[i] is the length of the ith stick.

# You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. You must connect all the sticks until there is only one stick remaining.

# Return the minimum cost of connecting all the given sticks into one stick in this way.


# Solution
# Time O(NlogN) as we perform heapify (LogN) for N times and space O(N) as we create a heap using array
# To get a minimum cost for connecting the sticks we need to connect two shortest sticks together until the number of sticks is not 1. Then we just return the accumulated cost.
import heapq
from typing import List


def connectSticks(sticks: List[int]) -> int:
    # minimum cost -> each time connect two minimum sticks
    if len(sticks) == 1:
        return 0

    cost = 0
    heapq.heapify(sticks)
    while len(sticks) > 1:
        first = heapq.heappop(sticks)
        second = heapq.heappop(sticks)
        cost += first + second
        heapq.heappush(sticks, first + second)
    return cost
