# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Difficulty: Easy (Medium)
# Tags: gcd string

# Problem
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Solution
# Time O(Log(Min(Len(Str1),Len(Str2)))) and space O(1)
# First we check if there is a common divisor for two strings. Then if there is, we use an euclidian algorithm for strings lengths to find the GCD (greatest common divisor).

def gcdOfStrings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""

    str1_n = len(str1)
    str2_n = len(str2)
    while str2_n:
        str1_n, str2_n = str2_n, str1_n % str2_n
    return str1[:str1_n]
