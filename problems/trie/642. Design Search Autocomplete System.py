# https://leetcode.com/problems/design-search-autocomplete-system/
# Difficulty: Hard
# Tags: trie autocomplete search

# Problem
# Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#').

# You are given a string array sentences and an integer array times both of length n where sentences[i] is a previously typed sentence and times[i] is the corresponding number of times the sentence was typed. For each input character except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

# Here are the specific rules:

#     The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
#     The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
#     If less than 3 hot sentences exist, return as many as you can.
#     When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.

# Implement the AutocompleteSystem class:

#     AutocompleteSystem(String[] sentences, int[] times) Initializes the object with the sentences and times arrays.
#     List<String> input(char c) This indicates that the user typed the character c.
#         Returns an empty array [] if c == '#' and stores the inputted sentence in the system.
#         Returns the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed. If there are fewer than 3 matches, return them all.

# Solution
# Time O(n⋅k+m⋅(n+m/k​)⋅log(n+m/k​)) and space O(k⋅(n⋅k+m))
# We use trie to solve this problem efficiently. We have a predefined dictionary of sentences, which we add to our trie and meanwhile updating the hash map for each node specifying the number of times sentence was inputted. It defines the hot level of each sentence. Autocomplete system must return top 3 hottest sentences that match the curr input at each character. So, we have to keep track of curr sentence and curr node in a trie. If the input character doesn't exist, we assign out current node to dead node, meaning no autocomplete can be done. In order to return hottest sentences we can either use sorting or max heap approach. Max heap is more efficient in terms of time complexity, so it's a preferred method. When the user inputs character '#' it means he finished inputting a sentence, so it can be added to the trie. All other variables must be reseted!

from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.curr_sentence = []
        for sentence, time in zip(sentences, times):
            self._insert(sentence, time)
        self.curr_node = self.root
        self.dead = TrieNode()  # deadend

    def _insert(self, sentence: str, times: int = 1):
        if not sentence:
            return

        curr = self.root
        for c in sentence:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.sentences[sentence] += times

    def input(self, c: str):
        if c == "#":
            self._insert("".join(self.curr_sentence), 1)
            self.curr_sentence = []
            self.curr_node = self.root
            return []

        self.curr_sentence.append(c)

        if c not in self.curr_node.children:
            self.curr_node = self.dead
            return []

        self.curr_node = self.curr_node.children[c]
        sentences = self.curr_node.sentences
        # str: int -> sentence: count
        sorted_sentences = sorted(
            sentences.items(), key=lambda x: (-x[1], x[0]))
        ans = []
        for i in range(min(3, len(sorted_sentences))):
            ans.append(sorted_sentences[i][0])
        # or heap
        # sentences = [(-val, key) for key, val in self.curr_node.sentences.items()]
        # heapq.heapify(sentences)
        # # str: int -> sentence: count
        # ans = []
        # for _ in range(3):
        #     if len(sentences) > 0:
        #         ans.append(heapq.heappop(sentences)[1])

        return ans


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
