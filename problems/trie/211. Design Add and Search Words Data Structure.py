# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Difficulty: Medium
# Tags: trie search dfs

# Problem
# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

#     WordDictionary() Initializes the object.
#     void addWord(word) Adds word to the data structure, it can be matched later.
#     bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


# Solution
# Time O(n) and space O(n)
# We use trie for efficient string adding and searching. For searching with wildcards, we use dfs in order to check all possible strings that match the wildcard.


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, index: int) -> bool:
            if index == len(word):
                return node.is_end_of_word

            ch = word[index]

            if ch == ".":
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False

            if ch not in node.children:
                return False

            return dfs(node.children[ch], index + 1)

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
