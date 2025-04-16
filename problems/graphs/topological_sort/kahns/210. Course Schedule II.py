# https://leetcode.com/problems/course-schedule-ii/
# Difficulty: Medium
# Tags: graph topological_sort kahns

# Problem
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

#     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# Solution
# Time O(V+E) and space O(V+E)
# We use Kahn's topological sort algorithm to solve this problem. First we have to create a `indegree` dictionary to count the indegrees for each vertex. Then we add an initial vertex with 0 indegrees to the queue. Next steps include decrementing indegrees for neighbouring nodes and adding to the queue next node with 0 indegrees. Repeat that step until queue is not empty and return topologically sorted array if it has the length same as the number of nodes (courses). If it isn't, that means it is impossible to finish all courses.

from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegree = defaultdict(int)
        graph = defaultdict(list)

        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1

        topological_sorted = []
        queue_no_indegree = deque(
            [node for node in range(numCourses) if node not in indegree])
        while queue_no_indegree:
            curr_node = queue_no_indegree.popleft()

            topological_sorted.append(curr_node)

            for nei in graph[curr_node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue_no_indegree.append(nei)

        return topological_sorted if len(topological_sorted) == numCourses else []
