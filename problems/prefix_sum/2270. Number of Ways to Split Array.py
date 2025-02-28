# https://leetcode.com/problems/number-of-ways-to-split-array/
# Difficulty: Medium
# Tags: prefix_sum

# Problem
# You are given a 0-indexed integer array nums of length n.

# nums contains a valid split at index i if the following are true:

#     The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
#     There is at least one element to the right of i. That is, 0 <= i < n - 1.

# Return the number of valid splits in nums.

# Solution
# Time O(n) and space O(n)
# We use prefix sum array for a more efficient sums search in this problem. Sum of first i+1 elements is a bit tricky as our array is 0-indexed, it will be prefix_sum[i], NOT prefix_sum[i+1]. And second sum is just a difference between total sum and first sum we calculated earlier. We can also use another approach without arrays, thus improving space complexity from O(n) to constant O(1).

from typing import List


def waysToSplitArray(nums: List[int]) -> int:
    n = len(nums)
    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    ans = 0
    total_sum = prefix_sum[-1]
    for i in range(n - 1):
        if prefix_sum[i] >= total_sum - prefix_sum[i]:
            ans += 1
    return ans


# or (even better)

def waysToSplitArray(nums: List[int]) -> int:
    ans = left = 0
    total = sum(nums)
    for i in range(len(nums) - 1):
        left += nums[i]
        right = total - left
        if left >= right:
            ans += 1
    return ans
