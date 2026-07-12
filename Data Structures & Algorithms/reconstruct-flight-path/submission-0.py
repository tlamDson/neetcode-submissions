from collections import defaultdict
import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        res = []
        for src, dst in tickets:
            heapq.heappush(adj[src], dst) 
        def dfs(u):
            while adj[u]:
                v = heapq.heappop(adj[u])
                dfs(v)
            res.append(u)
        dfs("JFK")
        return res[::-1]
            

        