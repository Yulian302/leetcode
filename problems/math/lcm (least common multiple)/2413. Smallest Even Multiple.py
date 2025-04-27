# https://leetcode.com/problems/smallest-even-multiple
# Difficulty: Easy
# Tags: lcm gcd even

# Problem
# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.

# Solution
# Time O(1) and space O(1).
# The easiest way for this case would be to check if number is even -> if it is, that would be the least common multiple of itself. Else the number multiplied by two would be the answer.

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        return n*2

# --- or --- (if we had more complex case (no checks if even))
# Time O(logN) and space O(1).
# This problem would be the problem to find least common multiple (lcm) or in other words smallest number that both `a` and `b` can be divided by. The formula for LCM is: `a * b // gcd(a, b)`, where gcd(a, b) is the Greatest Common Divisor/Factor of `a` and `b`.


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        # least common multiple = a * b / gcd(a,b)
        def gcd(a, b):
            while a > 0:
                a, b = b % a, a
            return b

        def lcm(a, b):
            return a * b // gcd(a, b)

        return lcm(n, 2)
