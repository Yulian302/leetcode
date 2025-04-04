# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# Difficulty: Medium
# Tags: heap max_heap matrix

# Problem
# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# You must find a solution with a memory complexity better than O(n2).


# Solution
# Time O(N^2*logK) and space O(K) as the heap doesn't grow beyond K elements
# We use max heap for this problem. The idea is to populate the max heap with elements and remain the size of a heap at most to K elements. Then, in the end, the root element in the heap will be the Kth smallest element in the matrix. For performance modifications: when we see - Kth smallest, we use max heap; when Kth largest -> we use min heap.


import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxHeap = []
        n = len(matrix)
        for row in range(n):
            for col in range(n):
                heapq.heappush(maxHeap, -matrix[row][col])

                while len(maxHeap) > k:
                    heapq.heappop(maxHeap)

        return -heapq.heappop(maxHeap)
