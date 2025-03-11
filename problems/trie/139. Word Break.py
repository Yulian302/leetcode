# https://leetcode.com/problems/word-break/
# Difficulty: Medium
# Tags: trie dp

# Problem
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.


# Solution
# We use trie to add each word in a word list. Then we init the dp array of input word size with init value of each element to False. We only move down the trie at the beginning (when we are at start of our input word) and when dp at previous i is True. Thus, we firstly move down the trie and if the word exists -> mark its end index as True. And in the end, we return dp[-1] which must be true if the input word can be constructed using words in dict.

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        for word in wordDict:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.is_end_of_word = True

        dp = [False] * len(s)
        for i in range(len(s)):
            if i == 0 or dp[i - 1]:
                curr = root
                for j in range(i, len(s)):
                    c = s[j]
                    if c not in curr.children:
                        break

                    curr = curr.children[c]
                    if curr.is_end_of_word:
                        dp[j] = True
        return dp[-1]
