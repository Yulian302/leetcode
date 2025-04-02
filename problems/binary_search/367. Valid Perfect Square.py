# https://leetcode.com/problems/valid-perfect-square/
# Difficulty: Medium
# Tags: binary_search perfect_square

# Problem
# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.


# Solution
# O(log2(N)) time and space O(1)
# We use binary search to look for a value that can form a num if squared. The searching range is [1,num]. Though it still can be divided by two to reduce it (making [1, num//2]), but as the time complexity is log2(N), it is not really neccessary. If the value doesn't exist, we return False. Important notice: simple binary search template can be implemented. The array is ascending, meaning it does not contain duplicates, result is a single element, so termination is: left<right.


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == num:
                return True
            elif square > num:
                right = mid - 1
            else:
                left = mid + 1
        return False
