# https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium
# Tags: anagrams hash_map defaultdict

# Problem
# Given an array of strings strs, group the

# together. You can return the answer in any order.


# Solution
# Time O(NKlogK) and space O(NK), where N is the number of strings and K is the maximum length in those strings.
# One of the ways to group anagrams is by their sorted strings. All anagrams would belong to the same group when sorted.

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)  # O(nk)
        for s in strs:  # O(nklogk)
            groups[tuple(sorted(s))].append(s)
        return list(groups.values())
