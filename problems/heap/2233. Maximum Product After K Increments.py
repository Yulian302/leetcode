# https://leetcode.com/problems/maximum-product-after-k-increments/
# Difficulty: Medium
# Tags: heap min_heap modulo

# Problem
# You are given an array of non-negative integers nums and an integer k. In one operation, you may choose any element from nums and increment it by 1.

# Return the maximum product of nums after at most k operations. Since the answer may be very large, return it modulo 109 + 7. Note that you should maximize the product before taking the modulo.

# Solution
# Time O(KlogN) and space O(N)
# In order to maximize the product we should choose the smallest number each time and increment it. Why? Let's say we have [0,4] where x=0, y=4 and x<y. If we choose to increment x: now we have (x+1)y = xy+y, otherwise we would have (y+1)x = xy+x. As x is smaller, the first equation would be greater and the second. So, we should increment x (the smallest number). We can use min heap for effectively working with smallest numbers. Plus, we have to use modulo operator each time we update our answer by multiplying it with every element. It is done to avoid number overflow/TLE for large numbers multiplication.

import heapq
from typing import List


def maximumProduct(nums: List[int], k: int) -> int:
    MOD = 1_000_000_007
    heapq.heapify(nums)

    for _ in range(k):
        heapq.heappush(nums, heapq.heappop(nums) + 1)

    ans = 1
    for num in nums:
        ans = (ans * num) % MOD
    return ans
