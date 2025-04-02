# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# Difficulty: Medium
# Tags: binary_search duplicates

# Problem
# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

# Solution
# O(log2(N)) time and space O(1)
# We use binary search to efficiently search for a smallest letter greater than target. As the array is sorted, binary search can be used. Non-decreasing order means we can have duplicates. Termination for this algo is left == right. In the end, left points at the next greatest letter if it exists, so we should also check it with an additional `if` statement.


from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        while left < right:
            mid = (left + right) // 2
            if ord(letters[mid]) > ord(target):
                right = mid
            else:
                left = mid + 1
        if ord(letters[left]) <= ord(target):
            return letters[0]
        else:
            return letters[left]
