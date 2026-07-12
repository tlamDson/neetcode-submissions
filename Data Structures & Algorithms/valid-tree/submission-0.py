class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = { i : [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u) # undirected edges so we add 2 dimension
        visited = set()
        def dfs(node,parent):
            if node in visited: 
                return False
            visited.add(node)
            for neighbor in adj[node]:
                # neu hang xom trung voi nut cha di qua -> bo qua bay vo huong
                if neighbor == parent:
                    continue
                if not dfs(neighbor,node):
                    return False
            return True
        if not dfs(0,-1):
            return False
        return len(visited) == n