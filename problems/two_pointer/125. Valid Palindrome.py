# Difficulty: Easy
# Tags: two_pointers palindrome

# Problem
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Solution
# Time O(n) and space O(1)
# At first we remove non alphanumeric characters from our string and convert it to lowercase. It takes O(n) of time and O(1) of space. Then we use two pointers technique to check if characters are equal from both sides. In this case middle char check is redundant.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
