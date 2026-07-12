class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [ 0 for i in range(len(edges) + 1)]
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x,y):
            rx, ry = find(x), find(y)
            if rx == ry: 
                return False
            if rank[rx] < rank[ry]:
                rx,ry = ry,rx
            parent[rx] = ry
            if rank[rx] == rank[ry]:
                rank[rx] += 1
            return True
        for x, y in edges:
            if not union(x,y):
                return [x,y]
        
        
            
        