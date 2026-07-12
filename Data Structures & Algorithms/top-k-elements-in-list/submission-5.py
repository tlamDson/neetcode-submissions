import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_dict = defaultdict(int)
        for num in nums:
            k_dict[num] += 1
        heap = []
        for num, freq in k_dict.items():
            heapq.heappush(heap, (freq,num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]
        
        