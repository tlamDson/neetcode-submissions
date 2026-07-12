"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        # cho 2 array start và end thì contians hết start và end times của all meeting
        # dùng 2 pointers s và e cho 2 array
        # count để track current number of active meeting
        # increaee s khi mà start time é hơn current end time
        # khi mà tăng e là khi khi meeting hết 
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        s, e = 0, 0
        count = 0
        max_rooms = 0
        while s <= len(start) - 1:
            if start[s] < end[e]:
                count += 1
                s += 1
                max_rooms = max(max_rooms, count)
            else:
                count -= 1
                e += 1
        return max_rooms
                


        