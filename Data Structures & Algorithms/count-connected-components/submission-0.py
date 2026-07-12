class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}

        for t,k in edges:
            adj[t].append(k)
            adj[k].append(t)
        visited = set()
        res = 0
        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        res = 0
        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            res += 1
        return res
            
                
        