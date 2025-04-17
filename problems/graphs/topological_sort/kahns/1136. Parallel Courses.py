# https://leetcode.com/problems/parallel-courses/
# Difficulty: Medium
# Tags: graph topological_sort kahns

# Problem
# You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.

# In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.

# Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.

# Solution
# Time O(N+E) and space O(N+E)
# We use Kahn's topological sort algorithm to solve this problem. First we have to create a `indegree` dictionary to count the indegrees for each vertex. Then we add an initial vertex with 0 indegrees to the queue. Next steps include decrementing indegrees for neighbouring nodes and adding to the queue next node with 0 indegrees. Repeat that step until queue is not empty and return topologically sorted array if it has the length same as the number of nodes (courses). If it isn't, that means it is impossible to finish all courses. We treat each level as single semester.

from collections import defaultdict, deque
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indegree = defaultdict(int)
        graph = defaultdict(list)

        for prerequisite, course in relations:
            graph[prerequisite - 1].append(course - 1)
            indegree[course - 1] += 1

        q = deque([i for i in range(n) if indegree[i] == 0])
        semesters = 0
        courses_taken = 0
        while q:
            semesters += 1
            n_queue = len(q)
            for _ in range(n_queue):
                course = q.popleft()
                courses_taken += 1

                for nei in graph[course]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
        return semesters if courses_taken == n else -1
