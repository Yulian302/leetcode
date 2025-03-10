# https://leetcode.com/problems/seat-reservation-manager/
# Difficulty: Medium
# Tags: heap min_heap seats

# Problem
# Design a system that manages the reservation state of n seats that are numbered from 1 to n.

# Implement the SeatManager class:

#     SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
#     int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
#     void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.


# Solution
# Time O(LogN) For Reserve,O(1) For Unreserve; and space O(N)For Both Reserve And Unreserve
# The clever way to solve this efficiently is to use a counter to track the next available seat and add unreserved to a min heap. Thus, when reserving, we check if the heap of unreserved is not empty and just pop from it.


import heapq


class SeatManager:

    def __init__(self, n: int):
        self.unreserved = []
        self.next_available = 1

    def reserve(self) -> int:
        if self.unreserved:
            return heapq.heappop(self.unreserved)
        else:
            seat = self.next_available
            self.next_available += 1
            return seat

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber < self.next_available:
            heapq.heappush(self.unreserved, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
