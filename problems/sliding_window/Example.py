# Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k. This is the problem we have been talking about above. We will now formally solve it.

# Solution
# Time O(n) and space O(1)
# We can utilize a sliding window approach for this problem and update our maximum length meanwhile.

def longest_subarray_sum_less_than_k(arr, k):
    left = curr = ans = 0
    for right in range(len(arr)):
        curr += arr[right]
        while curr > k:
            curr -= arr[left]
            left += 1
        ans = max(ans, right-left+1)
    return ans


print(longest_subarray_sum_less_than_k([1, 2, 3, 4, 5, 7, 8], 10))
