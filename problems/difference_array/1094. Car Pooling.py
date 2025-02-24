# https://leetcode.com/problems/number-of-enclaves/description/
# Difficulty: Medium
# Tags: difference array

# Problem
# A car has room for capacity passengers, and is given an array trips. Each trip is represented by [numPassengers, from, to], which indicates that at from, it picks up numPassengers, then drops them off at to. Can it complete all the trips without holding more passengers than capacity at any time?

# Solution
# O(n+m) time and space, where m is the maximum distance: m = max(trip[2] for trip in trips)
# First we create an array of a maximum distance from curr car position. As from and to are integers, that correspond to distances from curr car position to some predefined direction, we can create a difference array and find current passangers occupying the vehicle at given time. We add passangers at 'from' and subtract at 'to'. Next we check prefix sums to determine whether the limit was exceeded.
def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
    arr = [0] * (max(trip[2] for trip in trips) + 1)
    for val, left, right in trips:
        arr[left] += val
        arr[right] -= val
    curr = 0
    for i in range(len(arr)):
        curr += arr[i]
        if curr > capacity:
            return False
    return True
