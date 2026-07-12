class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # để không overlap thì nên xóa con mẹ nó đi 
        # ví dụ 1,2 2,4 1,4 2,3 thì sẽ là 1,2 1,4 2,3 2,4
        # 1,2 2,3 
        intervals.sort(key=lambda x: x[1])     
        i = 0 
        n = len(intervals)
        output = 0
        res = []
        while i < n:
            if not res:
                res.append(intervals[i])
            else:
                last_interval = res[-1]
                if last_interval[1] <= intervals[i][0]:
                    res.append(intervals[i])
                else:
                    output += 1
            i += 1
        return output
            
        