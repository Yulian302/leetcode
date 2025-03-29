# https://leetcode.com/problems/count-the-number-of-complete-components
# Difficulty: Medium
# Tags: graph bfs complete_components

# Problem
# You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

# Return the number of complete connected components of the graph.

# A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

# A connected component is said to be complete if there exists an edge between every pair of its vertices.

# Solution
# Time O(V+E) and space O(V)
# We use bfs to count the number of nodes and edges in a component. The thing is, the component is complete if the number of edges is equal to the number of nodes-1. Still for counting edges in bfs we should divide it by 2 in the end as each edge is visited twice. To compare the number of nodes and edges we should do the following comparison: (nodes * (nodes-1)) // 2 == edges

from collections import defaultdict, deque


class Solution:
    # edges - adjacency list (node1 -> node2)
    def countCompleteComponents(self, n: int, edges: list[(int, int)]):
        graph = defaultdict(list)
        # for undirected graph
        for x, y in edges:  # O(N)
            graph[x].append(y)
            graph[y].append(x)

        def bfs(node, seen):
            nodes = 1
            edges = 0
            seen.add(node)
            q = deque([node])
            while q:
                node = q.popleft()
                for nei in graph[node]:
                    edges += 1
                    if nei not in seen:
                        seen.add(nei)
                        nodes += 1
                        q.append(nei)
            return nodes, edges//2

        complete = 0
        seen = set()
        for i in range(n):
            if not i in seen:
                nodes, edges = bfs(i, seen)
                if edges == (nodes*(nodes-1))//2:
                    complete += 1
        return complete


sol = Solution()
print(sol.countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4]]))
