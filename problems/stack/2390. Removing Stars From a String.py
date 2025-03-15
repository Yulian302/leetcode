# https://leetcode.com/problems/removing-stars-from-a-string/
# Difficulty: Medium (easy)
# Tags: stack string

# Problem
# You are given a string s, which contains stars *.

# In one operation, you can:

#     Choose a star in s.
#     Remove the closest non-star character to its left, as well as remove the star itself.

# Return the string after all stars have been removed.

# Note:

#     The input will be generated such that the operation is always possible.
#     It can be shown that the resulting string will always be unique.


# Solution
# Time O(n) and space O(n)
# We use stack and add characters to it, if we meet a start, we simply pop from the stack.

def removeStars(s: str) -> str:
    stack = []

    for ch in s:
        if ch == "*":
            stack.pop()
        else:
            stack.append(ch)

    return "".join(stack)
