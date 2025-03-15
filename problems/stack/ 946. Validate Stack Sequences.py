# https://leetcode.com/problems/validate-stack-sequences/
# Difficulty: Medium
# Tags: stack greedy

# Problem
# Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

# Solution
# Time O(n+m) and space O(n)
# We populate stack in a greedy approach. When we meet the value equal to top of a stack, we pop it from the stack and update pointer for second array. Thus, if push and pop can be formed, the value of a j pointer will be len(popped).

from typing import List


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    stack = []
    j = 0
    for x in pushed:
        stack.append(x)
        while stack and j < len(popped) and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    return j == len(popped)
