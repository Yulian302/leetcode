# https://leetcode.com/problems/meeting-rooms-ii/
# Difficulty: Medium
# Tags: intervals min_heap

# Problem
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# Solution
# Time O(NlogN) and space O(N)
# First we sort the meetings by start time. Then we use min heap and add first meeting end time to keep track of min end time for curr meetings. Then if the next meeting's start time is more than curr min end time -> then we free the room (pop from heap). In the end we return the length of heap -> minimum number of rooms needed.

import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        free_rooms = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(free_rooms, intervals[0][1])

        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            heapq.heappush(free_rooms, i[1])

        return len(free_rooms)

# start times: 0 5 15
# free_rooms = [20, 30]
