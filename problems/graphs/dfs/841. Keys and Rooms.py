# https://leetcode.com/problems/keys-and-rooms/
# Difficulty: Medium
# Tags: graph dfs

# Problem
# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

# When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

# Solution
# Time O(n) and space O(n) because of recursion
# We use dfs to visit other rooms starting from room 0 while keeping track of visited rooms. Then we simply compare if number of visited rooms equals to number of rooms overall.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import List


def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    n = len(rooms)
    visited = set()

    def dfs(room):
        if room not in visited:
            visited.add(room)
            for key in rooms[room]:
                dfs(key)

    dfs(0)
    return len(visited) == n
