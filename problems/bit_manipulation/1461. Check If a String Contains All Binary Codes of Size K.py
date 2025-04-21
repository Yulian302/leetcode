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


# This approach is more efficient in time, but consumes more memory.
# Time O(N) and space O(2^K)
# It leverages efficient hashing technique that takes O(1) time to process each binary code.

def hasAllCodesRollingHash(s, k):
    need = 1 << k
    got = [False]*need
    all_one = need - 1
    hash_val = 0
    for i in range(len(s)):
        hash_val = ((hash_val << 1) & all_one | int(s[i]))
        if i >= k-1 and got[hash_val] is False:
            got[hash_val] = True
            need -= 1
            if need == 0:
                return True
    return False
