# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Difficulty: Easy
# Tags: interval

# Problem
# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

# Solution
# Time O(NlogN) and space O(1)
# First we sort our intervals by end time. Then we check one by one if end of first meeting is less than start of second meeting one by one.

from typing import List


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda x: x[1])
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False
    return True
