from collections import defaultdict, deque


class Solution:
    # edges - adjacency list (node1 -> node2)
    def countCompleteComponents(self, n: int, edges: list[(int, int)]):
        graph = defaultdict(list)
        # for undirected graph
        for x, y in edges:
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
