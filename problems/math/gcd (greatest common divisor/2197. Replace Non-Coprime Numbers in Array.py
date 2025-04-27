# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/
# Difficulty: Hard
# Tags: gcd stack merge

# Problem
# You are given an array of integers nums. Perform the following steps:

#     Find any two adjacent numbers in nums that are non-coprime.
#     If no such numbers are found, stop the process.
#     Otherwise, delete the two numbers and replace them with their LCM (Least Common Multiple).
#     Repeat this process as long as you keep finding two adjacent non-coprime numbers.

# Return the final modified array. It can be shown that replacing adjacent non-coprime numbers in any arbitrary order will lead to the same result.

# The test cases are generated such that the values in the final array are less than or equal to 108.

# Two values x and y are non-coprime if GCD(x, y) > 1 where GCD(x, y) is the Greatest Common Divisor of x and y.

# Solution
# Time O(nlogm) and space O(1)
# The most tricky part of this problem is to efficiently traverse the input array and substitute adjacent elements with their LCM if they are not coprime (gcd > 1). We can use stack for this part. Stack is initialized inside an outer for loop that iterates over the input array. It checks whether last added element and current are not coprime, then substitutes them and repeats that process unless they cannot be substituted again.

from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(a, b):
            while a:
                a, b = b % a, a
            return b

        stack = []

        for num in nums:
            current = num
            while stack:
                g = gcd(current, stack[-1])
                if g == 1:
                    break
                current = (current * stack[-1]) // g
                stack.pop()
            stack.append(current)

        return stack
