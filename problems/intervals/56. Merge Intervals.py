# https://leetcode.com/problems/merge-intervals/
# Difficulty: Medium
# Tags: interval merge

# Problem
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Solution
# Time O(n) and space O(n)
# We have to sort our arrays either by start time or end time. Then we create a merged array to populate with intervals. We traverse the input array and just append the interval if merged array is empty initially or the next interval does not overlap with the last in array (new start time is greater than old end time). Otherwise if they overlap, we update the last interval's end time with the max between two.

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
