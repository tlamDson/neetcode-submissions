import heapq
from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False]*n
        min_dist = [float('inf')]*n
        min_dist[0] = 0
        total = 0
        
        for _ in range(n):
            u = -1
            for i in range(n):
                if not visited[i] and (u==-1 or min_dist[i]<min_dist[u]):
                    u = i
            visited[u] = True
            total += min_dist[u]
            
            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0]-points[v][0]) + abs(points[u][1]-points[v][1])
                    min_dist[v] = min(min_dist[v], dist)
            
        return total