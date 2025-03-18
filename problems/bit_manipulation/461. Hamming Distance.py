# https://leetcode.com/problems/hamming-distance/
# Difficulty: Easy
# Tags: bit_manipulation xor hamming shift

# Problem
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, return the Hamming distance between them.

# Solution
# Time O(1) and space O(1) because the number of operations do not grow strongly regarding the input size.
# Firstly we use XOR operator to define the bits that are flipped (different). Then we count the number of ones just by checking the end of a binary number and shifting it to the right until it is zero. Meanwhile updating the count if the last element is 1.


def hammingDistance(x: int, y: int) -> int:
    # 0001 -> 1
    # 0100 -> 4
    # xor
    # 0101 -> count number of ones
    def count_ones(num):
        count = 0
        while num:
            count += num & 1  # plus one if ends with one
            num >>= 1  # shifting right to move to other bits
        return count

    return count_ones(x ^ y)
