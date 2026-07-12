from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = defaultdict(int)
        for num in nums:
            my_dict[num] += 1
        heap = []
        for num, freq in my_dict.items():
            heapq.heappush(heap, (freq,num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]
        

        

            



        
        
        