# https://leetcode.com/problems/count-primes/
# Difficulty: Medium
# Tags: prime sieve_of_eratosphenes

# Problem
# Given an integer n, return the number of prime numbers that are strictly less than n.

# Solution
# Time complexity O(sqrt(n)) and space O(n).
# The most efficient approach to count prime numbers in a range [2,n-1] is to use a Sieve of Eratosthenes. Numbers that are less than 2 cannot be prime numbers, so we return 0. Then we initialize an array of size n where arr[0] and arr[1] are False. This array shows whether ith number is a prime number. 0 and 1 are not prime numbers. Other elements must be set to True initially. Then we iterate over this array from 2 to sqrt(n) inclusive and apply Sieve of Eratosthenes. It says the following: If ith number is a prime number, then all its multipliers are not prime numbers, meaning each ith number from i*i to the end is not prime number. Here comes this loop:
# for j in range(i * i, n, i):
#     is_prime[j] = False
# Then, in the end, we simply sum this array up, which gives us the number of primes.


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)
