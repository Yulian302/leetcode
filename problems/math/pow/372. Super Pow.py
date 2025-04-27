# https://leetcode.com/problems/super-pow/
# Difficulty: Medium
# Tags: modulo pow

# Problem
# Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.


# Solution
# Time complexity O(L) and space O(L).
# The idea is following: x^1234567 = (x^123456)^10 * x^7, or more simple example: x^22 = (x^2)^10 * x^2. Knowing this, we can build a recursive formula. For finding pow, we can use a recursive formula: x^n = (x^(n/2))^(n/2) for even `n`, x^n = x*x^(n-1) for odd `n`. And of course we should apply modulo `m` for each overflowing operation.

from typing import List


class Solution:
    def powmod(self, x, n, m):
        if n == 0:
            return 1 % m
        elif n & 1 == 0:
            temp = self.powmod(x, n // 2, m)
            return (temp % m * temp % m) % m
        else:
            return (x % m * self.powmod(x, n - 1, m) % m) % m

    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        if not b:
            return 1
        return (
            self.powmod(self.superPow(a, b[:-1]), 10, MOD)
            % MOD
            * self.powmod(a, b[-1], MOD)
            % MOD
        ) % MOD
