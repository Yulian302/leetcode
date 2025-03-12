# https://leetcode.com/problems/solving-questions-with-brainpower/
# Difficulty: Medium
# Tags: dp max take_or_skip

# Problem
# You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

# The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.

#     For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
#         If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
#         If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.

# Return the maximum points you can earn for the exam.

# Solution
# Time O(n) and space O(n)

# Function dp(i) finds the max number of points to get at exam with i questions -> `state: i of type int, dp returns a number.`

# In order to solve the whole problem, we can first solve it's subproblems and derive the solution from them.
# We can either solve a question i and skip k next questions or skip question i and go to next question immediately. This is a classic take or skip problem. So, dp(i) = max(dp(i+1), questions[i][0]+dp(j)), where dp(i+1) is the max number of points we get if we skip current question; and questions[i][0]+dp(j) is if we choose to solve current question. For i out of bounds (>=n) we return 0 as those questions don't exist, thus you can't get points for them.


# For solving a dp, we use top-down (recursion with memoization) or bottom-up (iteratively fill up the dp array).
# The number of states for this problem is 1, so it's a 1D dp problem.
from typing import List


def mostPointsTopDown(questions: List[List[int]]) -> int:
    # dp(i) = 0 where i>=n
    # dp(i) = max(dp(i+1), questions[i][0]+dp(j)) where j=i+questions[i][1]+1
    n = len(questions)
    memo = {}

    def dp(i):  # max points for i questions

        if i >= n:
            return 0

        if i in memo:
            return memo[i]

        memo[i] = max(dp(i + 1), questions[i][0] + dp(i + questions[i][1] + 1))
        return memo[i]

    return dp(0)


def mostPointsBottomUp(questions: List[List[int]]) -> int:
    n = len(questions)
    dp = [0] * (n+1)
    for i in range(n-1, -1, -1):
        j = i + questions[i][1] + 1
        dp[i] = max(dp[i + 1], questions[i][0] + (dp[j] if j < n else 0))
    return dp[0]
