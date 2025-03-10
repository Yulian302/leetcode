# https://leetcode.com/problems/smallest-number-in-infinite-set/
# Difficulty: Medium
# Tags: heap min_heap set

# Problem
# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

# Implement the SmallestInfiniteSet class:

#     SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
#     int popSmallest() Removes and returns the smallest integer contained in the infinite set.
#     void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.


# Solution
# Time O(1)ForPopsmallest,O(1)ForAddbackO(1)ForPopsmallest,O(1)ForAddback; and space O(N)
# The clever way to solve this efficiently is to use a variable to track the smallest available number in an infinite set. We increment this variable when we call `pop` method. For `addBack` method we can use a min heap to store recovered numbers. Then when we pop again, we check if we have a minimum recovered number and return it if we do.

import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.smallestAvailable = 1
        self.recovered = []

    def popSmallest(self) -> int:
        if self.recovered:
            return heapq.heappop(self.recovered)
        else:
            smallest = self.smallestAvailable
            self.smallestAvailable += 1
            return smallest

    def addBack(self, num: int) -> None:
        if num < self.smallestAvailable and num not in self.recovered:
            heapq.heappush(self.recovered, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
