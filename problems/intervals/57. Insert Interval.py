# https://leetcode.com/problems/insert-interval/
# Difficulty: Medium
# Tags: interval

# Problem
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

# Solution
# Time O(n) and space O(n)
# We have our intervals sorted by start time. So, we can use binary search to efficiently find an insertion index of new interval. Then we insert in into given array. Then we iterate over intervals and append them to our resulting array: if the array is initially empty or the next interval do not overlap with the last in array, then we simply add it. Otherwise, if there is an overlap, we merge last interval with current just by changing the last interval end time to the max between two.

from typing import List


def insert(
    intervals: List[List[int]], newInterval: List[int]
) -> List[List[int]]:
    if not intervals:
        return [newInterval]

    n = len(intervals)
    target = newInterval[0]
    left, right = 0, n - 1
    res = []
    while left <= right:
        mid = (left + right) // 2
        if target > intervals[mid][0]:
            left = mid + 1
        else:
            right = mid - 1

    intervals.insert(left, newInterval)

    for interval in intervals:
        if not res or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])

    return res
