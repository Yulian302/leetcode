# https://leetcode.com/problems/implement-trie-ii-prefix-tree/
# Difficulty: Medium (premium)
# Tags: trie counts duplicates search

# Problem
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

#     Trie() Initializes the trie object.
#     void insert(String word) Inserts the string word into the trie.
#     int countWordsEqualTo(String word) Returns the number of instances of the string word in the trie.
#     int countWordsStartingWith(String prefix) Returns the number of strings in the trie that have the string prefix as a prefix.
#     void erase(String word) Erases the string word from the trie.

# Solution
# Time O(n) and space O(n)
# For this problme Trie data structure can be represented like that: Each Trie node has a character(value), its children - dict[char,TrieNode],'count' to count the number of words, and descendants_count to count the number of strings starting from this prefix. Thus, we avoid is_end_of_word and ch as they are redundant.


class Node:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.descendants_count = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        if not word:
            return

        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
            curr.descendants_count += 1
        curr.count += 1

    def countWordsEqualTo(self, word: str) -> int:
        if not word:
            return 0
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return 0
            curr = curr.children[ch]
        return curr.count

    def countWordsStartingWith(self, prefix: str) -> int:
        if not prefix:
            return 0
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return 0
            curr = curr.children[ch]
        return curr.descendants_count

    def erase(self, word: str) -> None:
        if not word:
            return

        curr = self.root
        for ch in word:
            curr = curr.children[ch]
            curr.descendants_count -= 1
        curr.count -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
