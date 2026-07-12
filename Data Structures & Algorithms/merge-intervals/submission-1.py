class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        res = []
        n = len(intervals)
        intervals.sort()
        while i < n:
            if not res:
                res.append(intervals[i])
            else:
                last_interval = res.pop()
                if last_interval[1] >= intervals[i][0]:
                    last_interval[0] = min(last_interval[0], intervals[i][0])
                    last_interval[1] = max(last_interval[1], intervals[i][1])
                    res.append(last_interval)
                else:
                    res.append(last_interval)
                    res.append(intervals[i])
            i += 1
        return res


    


            
        