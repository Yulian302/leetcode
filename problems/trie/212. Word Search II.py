# https://leetcode.com/problems/word-search-ii/
# Difficulty: Hard
# Tags: trie dfs backtracking

# Problem
# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.


# Solution
# We use trie data structure to solve this problem. At first we insert all words in a dictionary to the trie for an efficient prefix search. Then we iterate over a grid to find a letter that at least one word starts with in a dictionary. Then we call dfs with backtracking to check if the word can be matched. Some optimizations like word_ref at the end node of a word can be added.


from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word_ref = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if not word:
            return
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end_of_word = True
        curr.word_ref = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])

        trie = Trie()
        for word in words:
            trie.insert(word)

        found = set()

        def dfs(node, row, col, visited):
            if node.is_end_of_word:
                found.add(node.word_ref)

            if (row, col) in visited:
                return

            # check bounds
            if row < 0 or row >= m or col < 0 or col >= n:
                return

            # curr char
            char = board[row][col]

            # if word doesn't exist
            if char not in node.children:
                return

            # add to visited
            visited.add((row, col))

            # next node
            next_node = node.children[char]

            # explore in all directions
            for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                dfs(next_node, row + dy, col + dx, visited)

            # backtrack
            visited.remove((row, col))

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.root.children:
                    dfs(trie.root, i, j, set())
        return list(found)
