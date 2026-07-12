"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0: 
            return True
        intervals.sort(key = lambda x: x.end)
        last_taken = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i].start < last_taken.end:
                return False
            last_taken = intervals[i]
        return True
