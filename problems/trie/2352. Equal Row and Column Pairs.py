# https://leetcode.com/problems/equal-row-and-column-pairs/
# Difficulty: Medium
# Tags: trie hash_map matrix

# Problem
# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

# Solution
# Time O(N^2) and space O(N^2)
# Aside from plain hash map solution, we can also use trie to solve this problem. We can treat each number as a character (for trie it doesn't matter, as we perform efficient search).

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        root = TrieNode()

        for row in grid:
            curr = root
            for num in row:
                if num not in curr.children:
                    curr.children[num] = TrieNode()
                curr = curr.children[num]
            curr.count += 1

        count = 0

        for c in range(n):
            curr = root
            is_match = True
            for r in range(n):
                num = grid[r][c]
                if num not in curr.children:
                    is_match = False
                    break
                curr = curr.children[num]

            if is_match:
                count += curr.count

        return count
