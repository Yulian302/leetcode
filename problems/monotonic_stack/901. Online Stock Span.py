# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
# Difficulty: Medium
# Tags: stack monotonic_stack monotonic

# Problem
# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

# The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

#     For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
#     Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.

# Implement the StockSpanner class:

#     StockSpanner() Initializes the object of the class.
#     int next(int price) Returns the span of the stock's price given that today's price is price.


# Solution
# Time O(1) and space O(n)
# We can use a monotonic decreasing stack to solve this problem efficiently. If given price stores the property of a stack (less than or equal to the previous value), we simply return 1. Otherwise, we pop from the stack until the property is restored while incrementing span. We still have to store span in every stack element to access span for a corresponding element. This approach gives us O(1) time complexity for `next` method, though we still have a while loop.


class StockSpanner:

    def __init__(self):
        # decreasing monotonic stack
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
