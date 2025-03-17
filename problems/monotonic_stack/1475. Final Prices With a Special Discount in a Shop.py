# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
# Difficulty: Easy (medium)
# Tags: stack monotonic_stack monotonic

# Problem
# You are given an integer array prices where prices[i] is the price of the ith item in a shop.

# There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

# Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.


# Solution
# Time O(n) and space O(n)
# We can use a monotonic increasing stack of indexes in order to efficiently solve this problem in one pass (O(n)). First we create a copy of input array. Then we init a stack. We iterate over the input array and append elements to stack. If the property of a monotonic increasing stack is violated (meaning the next element is less than or equal to the top element in stack), then we pop the top stack element until the property is restored and meanwhile update our answer array by applying a discount. (answer[stack.pop()]-=prices[i])


from typing import List


def finalPrices(prices: List[int]) -> List[int]:
    # monotonic increasing stack
    stack = []
    answer = prices[:]
    for i in range(len(prices)):
        while stack and prices[i] <= prices[stack[-1]]:
            answer[stack.pop()] -= prices[i]
        stack.append(i)
    return answer


# --- or ---

# Brute Force O(n^2) and space O(n)
def finalPrices(prices: List[int]) -> List[int]:
    answer = prices[:]
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] <= prices[i]:
                answer[i] -= prices[j]
                break
    return answer
