import heapq
class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.large,num)
        convert = heapq.heappop(self.large)
        heapq.heappush(self.small, - convert)
        if len(self.small) > len(self.large):
            convert = -heapq.heappop(self.small)
            heapq.heappush(self.large,convert)
    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0
        return float(self.large[0])
            

        
        