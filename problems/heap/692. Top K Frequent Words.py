# https://leetcode.com/problems/top-k-frequent-words/
# Difficulty: Medium
# Tags: heap min_heap max_heap words frequency k

# Problem
# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

# Solution
# Time complexity: for max heap solution -> O(n+klogn), for min heap solution -> O(nlogk)
# Space complexity: for max heap -> O(n), for min heap -> O(n)

# We can use max heap with (freq, word) as elements thus getting top K most freq words lexicographically sorted. Or even better to use min heap and maintain the size of a heap not bigger than k elements and then sort in the end lexicographically.


# max heap
from collections import defaultdict
import heapq
from typing import Counter, List


def topKFrequent(words: List[str], k: int) -> List[str]:
    counter = Counter(words)  # O(n)
    max_heap = [(-freq, word) for word, freq in counter.items()]  # O(n)
    heapq.heapify(max_heap)  # O(n)
    return [heapq.heappop(max_heap)[1] for _ in range(k)]  # O(n+klogn)


# min heap

class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = defaultdict(int)
        for word in words:
            counter[word] += 1

        min_heap = []  # (freq, word)
        for word, freq in counter.items():
            heapq.heappush(min_heap, Pair(word, freq))
            while len(min_heap) > k:
                heapq.heappop(min_heap)

        return [p.word for p in sorted(min_heap, reverse=True)]
