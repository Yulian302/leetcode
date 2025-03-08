# https://leetcode.com/problems/remove-stones-to-minimize-the-total/
# Difficulty: Medium
# Tags: heap max_heap minimum

# Problem
# You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, and an integer k. You should apply the following operation exactly k times:

#     Choose any piles[i] and remove floor(piles[i] / 2) stones from it.

# Notice that you can apply the operation on the same pile more than once.

# Return the minimum possible total number of stones remaining after applying the k operations.

# floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).


# Solution
# Time O(NlogN+KlogK) and space O(N)
# In order to get the minimum number of stones after taking half of a pile of stones for k times, we need to take
# the largest pile each time. The most efficient way to do so it to use a max heap. It takes O(1) time to retrieve
# a pile and O(logN) time to reheapify the tree.

import heapq
from math import floor
from typing import List


def minStoneSum(piles: List[int], k: int) -> int:
    for i in range(len(piles)):
        piles[i] = -piles[i]

    heapq.heapify(piles)
    for i in range(k):
        # get max pile
        largest_pile = -heapq.heappop(piles)
        heapq.heappush(piles, -(largest_pile-floor(largest_pile/2)))

    return sum([-pile for pile in piles])
