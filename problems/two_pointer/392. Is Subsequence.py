# Difficulty: Easy
# Tags: two_pointers subsequence

# Problem
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Solution
# Time O(n+m) and space O(1)
# We use two pointers technique to go through both arrays. If the element on the left is equal to the element on the right, we move the left pointer. And eventually, if left array is a subsequence of a right array, our left pointer will be of length s.

def isSubsequence(s: str, t: str) -> bool:
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)
