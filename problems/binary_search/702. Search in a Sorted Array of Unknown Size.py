# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/
# Difficulty: Medium
# Tags: binary_search unknown_size

# Problem
# This is an interactive problem.

# You have a sorted array of unique elements and an unknown size. You do not have an access to the array but you can use the ArrayReader interface to access it. You can call ArrayReader.get(i) that:

#     returns the value at the ith index (0-indexed) of the secret array (i.e., secret[i]), or
#     returns 231 - 1 if the i is out of the boundary of the array.

# You are also given an integer target.

# Return the index k of the hidden array where secret[k] == target or return -1 otherwise.

# You must write an algorithm with O(log n) runtime complexity.


# Solution
# O(log2(N)) time and space O(1)
# We use binary search to find the target. The right bound is `target - value of first element` (worst-case). [kinda of a hack]

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:


class Solution:
    def search(self, reader: "ArrayReader", target: int) -> int:
        OUT_OF_BOUNDS = 2**31 - 1
        left = 0
        right = target - reader.get(0)
        while left <= right:
            mid = left + (right - left) // 2
            midElem = reader.get(mid)
            if midElem == OUT_OF_BOUNDS or midElem > target:
                right = mid - 1
            elif midElem == target:
                return mid
            else:
                left = mid + 1
        return -1
