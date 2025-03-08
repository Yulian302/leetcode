# https://leetcode.com/problems/minimum-genetic-mutation/
# Difficulty: Medium
# Tags: bfs genetic mutation

# Problem
# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

#     For example, "AACCGGTT" --> "AACCGGTA" is one mutation.

# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

# Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

# Note that the starting point is assumed to be valid, so it might not be included in the bank.

# Solution
# Time O(n) and space O(n)
# We use bfs for this problem. When trying to mutate the gene, the new mutated gene must be in a bank. So, this determines the way nodes are added in the bfs.

from collections import deque
from typing import List


def minMutation(startGene: str, endGene: str, bank: List[str]) -> int:

    if not bank:
        return -1

    mutations = 0
    choices = ["A", "C", "G", "T"]
    q = deque([startGene])
    bank = set(bank)
    if endGene not in bank:
        return -1
    seen = {startGene}
    while q:
        for _ in range(len(q)):
            gene = q.popleft()
            if gene == endGene:
                return mutations
            for i in range(len(gene)):
                for choice in choices:
                    if choice != gene[i]:
                        new_gene = gene[:i] + choice + gene[i + 1:]
                        if new_gene in bank and new_gene not in seen:
                            q.append(new_gene)
                            seen.add(new_gene)
        mutations += 1
    return -1
