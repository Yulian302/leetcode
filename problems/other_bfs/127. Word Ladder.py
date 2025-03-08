# https://leetcode.com/problems/word-ladder/
# Difficulty: Hard
# Tags: bfs words string

# Problem
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

#     Every adjacent pair of words differs by a single letter.
#     Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#     sk == endWord

# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.


# Solution
# Time O(n*m) and space O(n*m) as bfs only considers valid strings
# We use bfs to explore possible solutions and update the number of transformations. This is a common bfs pattern.

from collections import deque
from typing import List


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:

    alphabet = "abcdefghijklmnopqrstuvwxyz"  # 26
    q = deque([beginWord])
    wordList = set(wordList)

    if endWord not in wordList:
        return 0

    seen = {beginWord}
    transformations = 1
    while q:
        for _ in range(len(q)):
            curr_word = q.popleft()
            for i in range(len(curr_word)):
                for c in alphabet:
                    if c != curr_word[i]:
                        new_word = curr_word[:i] + c + curr_word[i + 1:]
                        if new_word == endWord:
                            return transformations + 1
                        if new_word in wordList and new_word not in seen:
                            seen.add(new_word)
                            q.append(new_word)
        transformations += 1
    return 0
