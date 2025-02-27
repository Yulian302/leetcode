# Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.

# Solution
# Time O(n) and space O(1)
# We use fixed sliding window to find sum of k-length subarray and update our maximum length variable.

def largestSubarraySumOfK(arr, k):
    if k > len(arr):
        return 0
    curr = 0
    for i in range(k):
        curr += arr[i]

    ans = curr

    for right in range(k, len(arr)):
        curr += arr[right] - arr[right-k]
        ans = max(ans, curr)
    return ans


print(largestSubarraySumOfK([2, 34, 5, 6, -2, 3, 4, 5], 4))
