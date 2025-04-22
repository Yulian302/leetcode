# https://leetcode.com/problems/permutations-iii/
# Difficulty: Medium
# Tags: backtracking permutations recursion

# Problem
# Given an integer n, an alternating permutation is a permutation of the first n positive integers such that no two adjacent elements are both odd or both even.

# Return all such alternating permutations sorted in lexicographical order.

# Solution
# Time O(N*N!) and space O(N*N!)
# We use the same backtracking algorithm as for generating permutations but now we also must check whether the last element in curr permutation has different parity. If not, just skip this element.

from typing import List


class Solution:
    def permute(self, n: int) -> List[List[int]]:

        def backtrack(curr):
            if len(curr) == n:
                ans.append(curr[:])
                return

            for i in range(1, n + 1):
                if i in curr or (len(curr) > 0 and curr[-1] % 2 == i % 2):
                    continue
                curr.append(i)
                backtrack(curr)
                curr.pop()

        ans = []
        backtrack([])
        return ans
