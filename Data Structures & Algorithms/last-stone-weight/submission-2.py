import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)     
        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            if second < first:
                heapq.heappush(max_heap,-(first-second))
        return 0 if len(max_heap) == 0 else -max_heap[0]          


        


            
        
        