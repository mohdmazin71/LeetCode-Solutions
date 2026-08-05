class Solution:
    def remainingMethods(self, n, k, invocations):
        # Build graph
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)

        # Mark suspicious methods using DFS
        suspicious = [False] * n

        def dfs(node):
            suspicious[node] = True
            for nei in graph[node]:
                if not suspicious[nei]:
                    dfs(nei)

        dfs(k)

        # If any non-suspicious method calls a suspicious method,
        # we cannot remove the suspicious methods.
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        # Return all non-suspicious methods
        ans = []
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans