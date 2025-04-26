# https://leetcode.com/problems/prime-arrangements/
# Difficulty: Easy (Medium)
# Tags: prime sieve_of_eratosphenes factorial permutations

# Problem
# Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

# (Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

# Since the answer may be large, return the answer modulo 10^9 + 7.

# Solution
# Time complexity O(sqrt(N)+N) = O(N) and space O(N).
# The overall number of possible permutations will be the product of prime number permutations and non-prime numbers permutations. To efficiently find the number of prime number from 1 to n, we can use Sieve of Eratosphenes. It takes sqrt(N) of time to find it. Then the number of permutations will be factorial of found numbers. So, we have: N = P1! * P2!, where P1 is the number of permutations of prime numbers and P2 is the number of permutations of non-prime numbers.

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        def count_primes(n: int):
            if n < 2:
                return 0

            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False

            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False

            return sum(is_prime)

        memo = {}

        def factorial(n):
            if n <= 0:
                return 1
            if n not in memo:
                memo[n] = n * factorial(n - 1) % MOD
            return memo[n]

        n_primes = count_primes(n)
        n_not_primes = n - n_primes
        return (factorial(n_primes) * factorial(n_not_primes)) % MOD
