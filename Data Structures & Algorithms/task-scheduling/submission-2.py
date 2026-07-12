import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        max_freq_count = 0
        for cnt in counts.values():
            if cnt == max_freq:
                max_freq_count += 1
        ans = (max_freq - 1)*(n+1) + max_freq_count
        return max(len(tasks),ans)
        