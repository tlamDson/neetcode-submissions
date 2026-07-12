import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k > len(points): return []
        if k == len(points): return points
        def distance(x,y):
            return x**2 + y**2

        heap = []
        for i,point in enumerate(points):
            heap.append([distance(point[0],point[1]),i])
        heapq.heapify(heap)
        res = []
        count = k
        while len(heap) > 0 and count > 0: 
            distance, i = heapq.heappop(heap)
            res.append(points[i])
            count -= 1
        return res

            

        