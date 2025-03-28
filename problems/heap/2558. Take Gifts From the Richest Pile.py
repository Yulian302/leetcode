# https://leetcode.com/problems/take-gifts-from-the-richest-pile/
# Difficulty: Easy
# Tags: heap max_heap

# Problem
# You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

#     Choose the pile with the maximum number of gifts.
#     If there is more than one pile with the maximum number of gifts, choose any.
#     Reduce the number of gifts in the pile to the floor of the square root of the original number of gifts in the pile.

# Return the number of gifts remaining after k seconds.


# Solution
# Time O(N+KlogN) and space: O(N) if we can't modify input in-place, O(1) - otherwise.
# The brute force method is obvious but we can use a max heap data structure for a more efficient max pile retrieval. For each operation we get the maximum gift pile and add floor(sqrt(maxPile)) back to the array of gifts. At the end we simply calculate the sum.


import heapq
from math import floor, sqrt
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]  # O(N)

        heapq.heapify(gifts)  # O(N)
        for _ in range(k):  # O(K)
            largestPile = -heapq.heappop(gifts)  # O(logN)
            heapq.heappush(gifts, -floor(sqrt(largestPile)))  # O(logN)

        return -sum(gifts)  # O(N)
