# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
# Difficulty: Medium
# Tags: binary codes

# Problem
# Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

# Solution
# Time O(N*K) and space O(N*K)
# The naive solution to this problem will be to iterate over the substrings of length k in the code and add it to the set. Then simply check if number of elements in the set is equal to 2^k, because we would have exactly 2^k possible binary codes of length k.

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # k = 2, 2^k codes
        n = len(s)
        codes = set()
        for i in range(n - k + 1):
            codes.add(s[i: i + k])
        return len(codes) == 2**k
