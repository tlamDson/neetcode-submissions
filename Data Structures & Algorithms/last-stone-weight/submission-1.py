import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = [-x for x in stones]  # Đổi thành [-3, -1, -5, -4]

        heapq.heapify(max_heap)     
        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            if first == second: 
                continue
            heapq.heappush(max_heap,- (first - second))
        if len(max_heap) == 0:
            return 0
        else:
            return -max_heap[0]            


        


            
        
        