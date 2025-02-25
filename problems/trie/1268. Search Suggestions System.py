# https://leetcode.com/problems/search-suggestions-system/
# Difficulty: Medium
# Tags: trie search

# Problem
# You are given an array of strings products and a string searchWord.

# Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

# Return a list of lists of the suggested products after each character of searchWord is typed.

# Solution
# Time O(nlogn+mlogn), where n is the number of words; m is a length of a search word. Space O(n)
# Trie data structure can be represented like that: Each Trie node has a character(value), its children - dict[char,TrieNode] and is_end_of_word to determine if it's the end of a word (used for searching words). In searchine we are moving down the trie and check if the last char of a word is the end. In prefix search, we do the same but don't check if it's the end of a word as it's redundant. NEW: We move over prefixes of our search word and seach for a given prefix in the Trie. Then, if it exists, we use either dfs or iterative approach (stack) to move down the tree with sorted keys to find existing words. Keys must be sorted to access found words lexicographically.

class TrieNode:
    def __init__(self, ch=""):
        self.ch = ch
        self.children = {}
        self.is_end_of_word = False


class Solution:
    def search_prefix_words(self, root, prefix) -> list:
        if not prefix:
            return
        ans = []
        curr = root
        for ch in prefix:
            if ch not in curr.children:
                return []
            curr = curr.children[ch]

        stack = [(curr, list(prefix))]
        while stack:
            node, path = stack.pop()

            if len(ans) == 3:
                return ans

            if node.is_end_of_word:
                ans.append("".join(path))

            for ch in sorted(node.children.keys(), reverse=True):
                stack.append((node.children[ch], path+[ch]))

        return ans

    def create_trie(self, words):
        if not words:
            return
        root = TrieNode()
        for word in words:
            if not word:
                continue
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode(ch)
                curr = curr.children[ch]
            curr.is_end_of_word = True
        return root

    def suggestedProducts(
        self, products: list[str], searchWord: str
    ) -> list[list[str]]:
        ans = []
        trie = self.create_trie(products)
        for i in range(len(searchWord)):
            ans.append(self.search_prefix_words(trie, searchWord[:i+1]))
        return ans
