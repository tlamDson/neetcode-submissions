class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        i = 0
        res = []
        intervals.sort()
        while i < len(intervals):
            if not res:
                res.append(intervals[i])
            else:
                last_interval = res[-1]
                if last_interval[1] >= intervals[i][0]:
                    last_interval[1] = max(last_interval[1], intervals[i][1])
                else:
                    res.append(intervals[i])
            i += 1
        return res


    


            
        