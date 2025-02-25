# https://leetcode.com/problems/implement-trie-prefix-tree/
# Difficulty: Medium
# Tags: trie

# Problem
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

#     Trie() Initializes the trie object.
#     void insert(String word) Inserts the string word into the trie.
#     boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
#     boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.


# Solution
# Trie data structure can be represented like that: Each Trie node has a character(value), its children - dict[char,TrieNode] and is_end_of_word to determine if it's the end of a word (used for searching words). In searchine we are moving down the trie and check if the last char of a word is the end. In prefix search, we do the same but don't check if it's the end of a word as it's redundant.

class TrieNode:
    def __init__(self, ch=""):
        self.ch = ch
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        if not word:
            return
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode(ch)
            curr = curr.children[ch]
        curr.is_end_of_word = True

    def search(self, word: str):
        if not word:
            return False
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.is_end_of_word

    def startsWith(self, prefix: str):
        if not prefix:
            return False
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True
