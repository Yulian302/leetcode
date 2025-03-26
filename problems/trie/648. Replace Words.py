# https://leetcode.com/problems/replace-words/
# Difficulty: Medium
# Tags: trie words replace

# Problem
# In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

# Return the sentence after the replacement.

# Solution
# Time O(K*Avg(w)+N*Avg(w)) and space O(K*Avg(w)+N*Avg(w))
# We use a Trie data structre to solve this problem. While searching for a prefix, we do early substitute when the word exists. Otherwise, the function returns None and curr word is not substituted with root and remains the same.

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if not word:
            return
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

        curr.is_end_of_word = True

    def substitute(self, word):
        if not word:
            return None
        curr_path = []
        curr = self.root
        for ch in word:
            if curr.is_end_of_word:
                return "".join(curr_path)
            curr_path.append(ch)
            if ch not in curr.children:
                return None
            curr = curr.children[ch]
        return None

# size(dict) - K
# size(sent) - N


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        res = []
        trie = Trie()
        for word in dictionary:  # O(K*Avg(len(word)))
            trie.insert(word)

        for word in sentence.split(" "):  # O(N*Avg(len(word)))
            sub = trie.substitute(word)
            res.append(sub if sub else word)
        return " ".join(res)
