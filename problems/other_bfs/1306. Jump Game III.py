# https://leetcode.com/problems/jump-game-iii/
# Difficulty: Medium
# Tags: bfs jump_game

# Problem
# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

# Notice that you can not jump outside of the array at any time.

# Solution
# Time O(n) and space O(n)
# We use bfs for this problem. We only add those jumps that are inbounds and keep track of visited nodes to avoid infinite loop. Then just return true when element we jumped at is 0. Otherwise, if it's impossible, we return false.

from collections import deque
from typing import List


def canReach(arr: List[int], start: int) -> bool:

    n = len(arr)
    # (idx)
    q = deque([start])
    # (idx)
    seen = {start}
    while q:
        for _ in range(len(q)):
            curr_idx = q.popleft()
            if arr[curr_idx] == 0:
                return True
            jump_front = curr_idx+arr[curr_idx]
            if jump_front < n and jump_front not in seen:
                seen.add(jump_front)
                q.append(curr_idx+arr[curr_idx])
            jump_back = curr_idx-arr[curr_idx]
            if jump_back >= 0 and jump_back not in seen:
                seen.add(jump_back)
                q.append(curr_idx-arr[curr_idx])
    return False
