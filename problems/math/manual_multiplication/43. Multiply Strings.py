# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Difficulty: Medium
# Tags: manual_multiplication strings

# Problem
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Solution
# Time O()
# In order to solve this problem we have to manually multiply two numbers that are represented as strings. First we reverse the strings of each number. Then we define a function that returns a sum for a curr digit and a number. We use mod operator and // division to handle remainder etc. Just a manual multiplication simulation. Then we get three reversed number that must be summed up with another function. Then we reverse the final array, convert it to string and get the result.


from itertools import zip_longest


class Solution:
    def multiply_one_digit(self, digit2, num_zeros, first_number) -> list[int]:
        curr_res = [0] * num_zeros
        carry = 0
        digit2 = ord(digit2) - ord("0")
        for digit1 in first_number:
            digit1 = ord(digit1) - ord("0")
            multiplication = digit2 * digit1 + carry
            carry = multiplication // 10
            curr_res.append(multiplication % 10)

        if carry != 0:
            curr_res.append(carry)

        return curr_res

    def sum_results(self, results: list[list[int]]):
        answer = results.pop()
        for result in results:
            new_answer = []
            carry = 0
            for digit1, digit2 in zip_longest(result, answer, fillvalue=0):
                curr_sum = digit1 + digit2 + carry
                carry = curr_sum // 10
                new_answer.append(curr_sum % 10)

            if carry != 0:
                new_answer.append(carry)

            answer = new_answer
        return answer

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        first_number = num1[::-1]
        second_number = num2[::-1]

        results = []

        for index, digit in enumerate(second_number):
            results.append(self.multiply_one_digit(digit, index, first_number))

        answer = self.sum_results(results)
        return "".join(str(digit) for digit in reversed(answer))
