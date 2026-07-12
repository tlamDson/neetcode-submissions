from collections import Counter
class CountSquares:


    def __init__(self):
        self.points = Counter()
        

    def add(self, point: List[int]) -> None:
        x,y = point
        self.points[(x,y)] += 1
        

    def count(self, point: List[int]) -> int:
        qx, qy = point
        ans = 0
        for (x,y), freq in self.points.items():
            if abs(x - qx) != abs(y-qy) or x == qx:
                continue
            ans += ( freq * self.points[(qx,y)]* self.points[(x, qy)])
        return ans
        
