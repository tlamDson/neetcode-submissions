"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Tạo danh sách mới đã được sắp xếp từ tuple
        if not intervals: return True
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        prevEnd = sorted_intervals[0].end
        for i in range(1, len(intervals)):
            if prevEnd > sorted_intervals[i].start:
                return False
            prevEnd = sorted_intervals[i].end
        return True


        
