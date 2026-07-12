import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((v,t))
        visited = set()
        # hướng giải bài này là đi từ điểm đầu qua các điểm cuối 
        # dùng min heap để mà gọi là lưu các giá trị thôi
        # khởi tạo bảng lưu giá trị ngắn nhất
        dist = {i: float('inf') for i in range(1, n + 1)}
        # giá trị đầu tiên là 0
        dist[k] = 0
        min_heap = [(0,k)]
        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            for neighbor, t in adj[node]:
                if neighbor in visited:
                    continue
                new_time = time + t
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                heapq.heappush(min_heap, (new_time, neighbor))
        if len(visited) == n:
            return max(dist.values())
        else:
            return -1

                
                
                
            