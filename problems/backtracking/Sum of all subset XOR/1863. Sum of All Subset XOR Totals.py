# https://leetcode.com/problems/sum-of-all-subset-xor-totals/
# Difficulty: Easy (medium)
# Tags: backtracking subsets xor

# Problem
# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

#     For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.

# Given an array nums, return the sum of all XOR totals for every subset of nums.

# Note: Subsets with the same elements should be counted multiple times.

# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

# Solution
# Time O(N*2^N) and space O(N*2^N)
# We use backtracking for this problem. Variables for backtracking function are `curr_index` and `curr_xor`. We use DFS to go down the tree, calculating the XOR of all elements. When curr index is of length of array, we add it to total and return. Then we backtrack, calling a recursive function without including the curr index xor. Thus, we calculate xors of all subsets and add them to total.

from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(index, curr_xor):
            nonlocal total
            if index == len(nums):
                total += curr_xor
                return

            backtrack(index + 1, curr_xor ^ nums[index])
            backtrack(index + 1, curr_xor)

        total = 0
        backtrack(0, 0)
        return total
