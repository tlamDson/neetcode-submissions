import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
            
        # stops_tracker[i] lưu số điểm dừng tối thiểu đã dùng để tới đỉnh i
        # Khởi tạo là vô cực
        stops_tracker = [float('inf')] * n
        
        # (chi_phí, đỉnh_hiện_tại, số_điểm_dừng_đã_dùng)
        minheap = [(0, src, 0)]
        
        while minheap:
            cost, u, stops = heapq.heappop(minheap)
            
            # Nếu tới đích, trả về cost
            if u == dst:
                return cost
            
            # Nếu số điểm dừng hiện tại đã đạt k, không đi tiếp được nữa
            if stops > k:
                continue
                
            # Chỉ xét tiếp nếu đường đi này tối ưu hơn đường cũ về số điểm dừng
            if stops < stops_tracker[u]:
                stops_tracker[u] = stops
                
                for v, weight in adj[u]:
                    heapq.heappush(minheap, (cost + weight, v, stops + 1))
            
        return -1