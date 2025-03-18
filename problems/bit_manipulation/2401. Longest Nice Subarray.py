# https://leetcode.com/problems/longest-nice-subarray/
# Difficulty: Medium
# Tags: sliding_window bitwise bitmask xor

# Problem
# You are given an array nums consisting of positive integers.

# We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

# Return the length of the longest nice subarray.

# A subarray is a contiguous part of an array.

# Note that subarrays of length 1 are always considered nice.

# Solution
# Time O(n) and space O(1)
# We use sliding window approach. It's a common pattern, but we have to focus on some advanced bit manipulation concepts used here. We initialize bitmask to 0 and check for the nice subarray (AND operation of numbers represented in bits must be 0). At each operation, we have to use logical OR to update the changed bits. If we have violated the property, meaning if & (AND) operation on curr and current number is not 0, then we have to unset the bits using XOR operation on curr with the number at left pointer.
# Basically, XOR can unset a bit. Meaning, if the bit was 0, now it will be 1 and vice verse. Zeros in XOR just copy the old bits -> 5 ^ 0 = 5 and 5 ^ 1 = 4 (0b100)

from typing import List


def longestNiceSubarray(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 1

    left = 0
    bitmask = 0
    ans = 0
    for right in range(n):
        while (bitmask & nums[right]) != 0:
            bitmask ^= nums[left]
            left += 1
        bitmask |= nums[right]
        ans = max(ans, right - left + 1)
    return ans
