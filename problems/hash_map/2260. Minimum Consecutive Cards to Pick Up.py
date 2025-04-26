# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/
# Difficulty: Medium
# Tags: hash_map index_map

# Problem
# You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

# Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.

# Solution
# Time O(N) and space O(N).
# We can use hash map to solve this problem in one run. Hash map would consist of `card: count` as key:value pairs. For each card, we set it's first occurence index. Then, if a card is already in the hash map, we update the minimum distance (number of cards to pickup) and set previous card occurence to current index. Thus, we efficiently find the minimum number of cards to pickup without duplicates.


from cmath import inf
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # card: count
        # 3:3
        # 4:1
        # 2:2
        map_ = {}
        smallest = inf
        for i, card in enumerate(cards):
            if card in map_:
                smallest = min(smallest, i - map_[card] + 1)
                map_[card] = i
                continue
            map_[card] = i
        return smallest if smallest != inf else -1
