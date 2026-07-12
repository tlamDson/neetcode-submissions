import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)
        t = 0
        q = deque()
        while heap or q:
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt != 0:
                    q.append((cnt, t + n))
            if q and q[0][1] == t:
                heapq.heappush(heap,q.popleft()[0])
            t += 1
        return t


        