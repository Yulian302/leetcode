# https://leetcode.com/problems/find-the-town-judge/
# Difficulty: Easy
# Tags: graph

# Problem
# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

#     The town judge trusts nobody.
#     Everybody (except for the town judge) trusts the town judge.
#     There is exactly one person that satisfies properties 1 and 2.

# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.


# Solution
# Time O(n) and space O(n)
# In order to find a town judge we have to find a node with no outbound edges and n-1 inbound edges. Thus, the town judge don't trust anybody and everybody trusts him.

from collections import defaultdict
from typing import List


def findJudge(n: int, trust: List[List[int]]) -> int:

    if n == 1:
        return 1

    trusts = defaultdict(list)
    trusted_by = defaultdict(int)

    for a, b in trust:
        trusts[a].append(b)
        trusted_by[b] += 1

    for i in range(1, n + 1):
        if len(trusts[i]) == 0 and trusted_by[i] == n - 1:
            return i
    return -1
