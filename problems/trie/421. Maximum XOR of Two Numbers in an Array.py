# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
# Difficulty: Medium
# Tags: trie bitwise bitwise_trie

# Problem
# Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

# Solution
# Time O(32*N)=O(N) and space O(2^L)=O(M)=O(1)
# We can use a bitwise trie to solve this problem. First we have to find the longest binary number representation and add padding to other binary numbers. Then we create a bitwise trie from input nums and while populating we are trying to go through the toggled bit each time we move down the trie. After each number insertion, we update our maximum found xor so far.

from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        L = len(bin(max(nums))) - 2

        nums = [[(x >> i) & 1 for i in range(L)][::-1] for x in nums]

        max_xor = 0
        trie = {}
        for num in nums:
            node = trie
            xor_node = trie
            curr_xor = 0
            for bit in num:
                if not bit in node:
                    node[bit] = {}
                node = node[bit]
                toggled_bit = 1 - bit
                if toggled_bit in xor_node:
                    curr_xor = (curr_xor << 1) | 1
                    xor_node = xor_node[toggled_bit]
                else:
                    curr_xor = curr_xor << 1
                    xor_node = xor_node[bit]

            max_xor = max(max_xor, curr_xor)

        return max_xor
