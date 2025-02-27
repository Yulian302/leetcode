# You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?

# For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.

# Solution
# Time O(n) and space O(1)
# We utilize sliding window approach for this problem. As we can flip only one "0" to "1", we should count overall zeros for our substring and then shrink window from left while number of zeros is more than 1.
def longest_ones(s):
    left = curr = ans = 0
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right-left+1)
    return ans


print(longest_ones("001110111100"))
