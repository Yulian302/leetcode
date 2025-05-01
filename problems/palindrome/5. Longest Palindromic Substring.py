# https://leetcode.com/problems/longest-palindromic-substring/
# Difficulty: Medium
# Tags: palindrome longest

# Problem
# Given a string s, return the longest palindromic substring in s.

# Solution
# Time O(n^2) and space O(1)
# We use the idea of extending from a center. For current index, there can be an odd length palindrome with center at (i,i) or even length palindrome at (i,i+1). So, for each index we initilize an expansion from center for both odd and even cases and update the maximum found window.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_center(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            i += 1
            j -= 1
            return j - i + 1

        ans = [0, 0]
        for i in range(len(s)):
            odd_length = expand_center(i, i)
            if odd_length > ans[1] - ans[0] + 1:
                dist = odd_length // 2
                ans = [i - dist, i + dist]

            even_length = expand_center(i, i + 1)
            if even_length > ans[1] - ans[0] + 1:
                dist = (even_length // 2) - 1
                ans = [i - dist, i + 1 + dist]
        i, j = ans
        return s[i: j + 1]
