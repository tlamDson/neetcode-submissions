from collections import defaultdict
from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.my_dict = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.my_dict[key].append([timestamp,value])
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.my_dict:
            return ""
        values = self.my_dict[key]
        idx = bisect_right(values,timestamp, key = lambda x : x[0])
        if idx == 0:
            return ""
        return values[idx-1][1]
        
