# https://leetcode.com/problems/furthest-building-you-can-reach/
# Difficulty: Medium
# Tags: heap min_heap greedy

# Problem
# You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

# You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

# While moving from building i to building i+1 (0-indexed),

#     If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
#     If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.

# Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.


# Solution
# Time O(NlogN) or O(NlogL) and space O(N) or O(L) depending on the number of ladders.
# We should use min heap to solve this problem. At first steps we use all available ladders, pushing climbs to min heap. Then when we are out of ladders, we check the curr climb: 1) If it's less than a minimum climb in a heap of allocated ladders, then we use bricks. 2) If it's more than a minimum climb in a heap of allocated ladders, then we have to substitute this climb with a ladder and use bricks where we used to use a ladder. When we have a negative number of bricks available, then we return i - the furthest point we can get to.


import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # min heap
        ladder_allocations = []
        n = len(heights)
        for i in range(n - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue
            # we have to use either bricks or ladders
            # if we have ladders
            if ladders > 0:
                heapq.heappush(ladder_allocations, climb)
                ladders -= 1
            else:  # there are no ladders left

                if ladder_allocations and climb > ladder_allocations[0]:
                    bricks -= heapq.heappop(ladder_allocations)
                    heapq.heappush(ladder_allocations, climb)
                else:
                    # Use bricks directly
                    bricks -= climb

                if bricks < 0:
                    return i
        return len(heights) - 1
