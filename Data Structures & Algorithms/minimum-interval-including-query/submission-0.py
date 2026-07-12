import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # 1. Sắp xếp intervals theo start time
        intervals.sort()
        
        # 2. Sắp xếp queries nhưng lưu index để trả về đúng thứ tự
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        
        res = [-1] * len(queries)
        min_heap = [] # Lưu (length, end)
        i = 0
        
        for q, original_idx in sorted_queries:
            # 3. Đưa tất cả các khoảng có start <= q vào heap
            while i < len(intervals) and intervals[i][0] <= q:
                length = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(min_heap, (length, intervals[i][1]))
                i += 1
            
            # 4. Loại bỏ các khoảng đã kết thúc (end < q)
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            # 5. Nếu heap còn, phần tử nhỏ nhất chính là khoảng ngắn nhất bao quanh q
            if min_heap:
                res[original_idx] = min_heap[0][0]
                
        return res