# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
# Difficulty: Easy (medium)
# Tags: heap max_heap k

# Problem
# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

# A row i is weaker than a row j if one of the following is true:

#     The number of soldiers in row i is less than the number of soldiers in row j.
#     Both rows have the same number of soldiers and i < j.

# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

# Solution
# Time O(M*N*logK) and space O(logK)
# We use max heap to keep track of K weakest rows. To break the tie, we make a row with a smaller index weaker, so we have to include it in a max heap as well.

import heapq
from typing import List


def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    maxHeap = []
    m = len(mat)
    n = len(mat[0]) if m > 0 else 0
    for row in range(m):
        nSoldiers = 0
        for col in range(n):
            if mat[row][col] == 1:
                nSoldiers += 1
            else:
                break
        heapq.heappush(maxHeap, (-nSoldiers, -row))

        while len(maxHeap) > k:
            heapq.heappop(maxHeap)

    weakest = []
    for _ in range(k):
        soldiers, row = heapq.heappop(maxHeap)
        weakest.append((-soldiers, -row))
    weakest.sort()

    return [row for _, row in weakest[:k]]
