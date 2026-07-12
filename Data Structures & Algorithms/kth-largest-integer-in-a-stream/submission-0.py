import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        # 1. Turn the list into a heap in-place: O(N)
        heapq.heapify(self.heap)
        
        # 2. Keep only the k largest elements
        # Pop the smallest until only k are left
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # 3. Add the new value
        heapq.heappush(self.heap, val)
        
        # 4. If we have more than k, remove the smallest
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # 5. The root (top) of the min-heap is now the Kth largest
        return self.heap[0]