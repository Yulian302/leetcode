# https://leetcode.com/problems/open-the-lock/
# Difficulty: Medium
# Tags: bfs lock

# Problem
# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

# The lock initially starts at '0000', a string representing the state of the 4 wheels.

# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

# Solution
# Time O(10^4) and space O(10^4)
# We use bfs for this problem to go through possible solutions. If we get into a deadend, -1 is returned. Else we explore all possible combinations.

from collections import deque
from typing import List


def openLock(deadends: List[str], target: str) -> int:

    visited_combs = set(deadends)
    if "0000" in visited_combs:
        return -1
    next_number = {
        "0": "1",
        "1": "2",
        "2": "3",
        "3": "4",
        "4": "5",
        "5": "6",
        "6": "7",
        "7": "8",
        "8": "9",
        "9": "0",
    }
    prev_number = {
        "0": "9",
        "1": "0",
        "2": "1",
        "3": "2",
        "4": "3",
        "5": "4",
        "6": "5",
        "7": "6",
        "8": "7",
        "9": "8",
    }

    turns = 0
    pending_combs = deque(["0000"])
    visited_combs.add("0000")
    while pending_combs:
        n_nodes = len(pending_combs)
        for _ in range(n_nodes):
            curr_comb = pending_combs.popleft()
            if curr_comb == target:
                return turns

            for wheel in range(4):
                new_comb = list(curr_comb)
                new_comb[wheel] = next_number[new_comb[wheel]]
                new_comb_str = "".join(new_comb)
                if new_comb_str not in visited_combs:
                    visited_combs.add(new_comb_str)
                    pending_combs.append(new_comb_str)

                new_comb = list(curr_comb)
                new_comb[wheel] = prev_number[new_comb[wheel]]
                new_comb_str = "".join(new_comb)
                if new_comb_str not in visited_combs:
                    visited_combs.add(new_comb_str)
                    pending_combs.append(new_comb_str)

        turns += 1
    return -1
