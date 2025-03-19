# https://leetcode.com/problems/find-the-divisibility-array-of-a-string/
# Difficulty: Medium
# Tags: modulo div

# Problem
# You are given a 0-indexed string word of length n consisting of digits, and a positive integer m.

# The divisibility array div of word is an integer array of length n such that:

#     div[i] = 1 if the numeric value of word[0,...,i] is divisible by m, or
#     div[i] = 0 otherwise.

# Return the divisibility array of word.


# Solution
# Time complexity O(n) and space O(n).
# In order to solve this problem and avoid overflowing and TLE for converting large numbers/working with large numbers, we can use modulo operator. In fact, we can set up curr to 0 and iterate over prefixes using the following logic: curr = ((curr*10) + digit) % m. Thus, we can check if digit is divisable by m and populate the resulting array with 1. Otherwise, we set 0. The hard part is the mod operator trick. If we meet a digit which is not divisable by m (num % m != 0), our curr gets updated to the remainded of division and that remainder is used for consequent operations (curr * 10 + digit).

from typing import List


def divisibilityArray(word: str, m: int) -> List[int]:
    n = len(word)
    div = [0] * n
    curr = 0
    i = 0
    for digit in word:
        curr = ((curr * 10) + int(digit)) % m
        if curr == 0:
            div[i] = 1
        else:
            div[i] = 0
        i += 1
    return div
