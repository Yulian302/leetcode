# https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Tags: hash_map anagram

# Problem
# Given two strings s and t, return true if t is an of s, and false otherwise.

# Solution
# Time O(n) and space O(n)
# We use hash map to keep track of the number of each symbol in first word, then after removing them from second word we check if hash map is empty.

from collections import defaultdict


def isAnagram(s: str, t: str) -> bool:
    d = defaultdict(int)
    for ch in s:
        d[ch] += 1
    for ch in t:
        d[ch] -= 1
        if d[ch] == 0:
            del d[ch]
    return len(d) == 0
