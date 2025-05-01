# https://leetcode.com/problems/gray-code/
# Difficulty: Medium
# Tags: backtracking gray_code bit_manipulation

# Problem
# An n-bit gray code sequence is a sequence of 2n integers where:

#     Every integer is in the inclusive range [0, 2n - 1],
#     The first integer is 0,
#     An integer appears no more than once in the sequence,
#     The binary representation of every pair of adjacent integers differs by exactly one bit, and
#     The binary representation of the first and last integers differs by exactly one bit.

# Given an integer n, return any valid n-bit gray code sequence.

# Solution
# Time O(N*2^N) and space O(2^N)
# We use backtracking for this problem. A neat trick to find if binary codes are adjacent is to find a binary code with 1 in place of where bits are different (simple xor operator) and do `x & (x-1) == 0` instead of counting a number of ones which is long. We generate bits same as for permutations, but to make it more efficient we work with decimal number and convert them to binary codes, so that it creates O(N) loop, but not O(2^N). At the end, when we reach base case, we still need to check circular property. Only if it returns True, we return this answer, else we have to move up the recursive tree and explore other candidates.

from typing import List


class Solution:
    def isAdjacent(self, a, b):
        x = a ^ b
        return x != 0 and (x & (x - 1)) == 0

    def grayCode(self, n: int) -> List[int]:
        used = {0}
        result = [0]

        def backtrack():
            if len(result) == (1 << n):
                return self.isAdjacent(result[0], result[-1])

            last = result[-1]
            for i in range(n):
                nextNum = last ^ (1 << i)
                if nextNum in used or not self.isAdjacent(last, nextNum):
                    continue

                used.add(nextNum)
                result.append(nextNum)
                if backtrack():
                    return True
                result.pop()
                used.remove(nextNum)

            return False

        backtrack()
        return result
