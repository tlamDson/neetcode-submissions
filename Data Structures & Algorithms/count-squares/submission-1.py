from collections import defaultdict
class CountSquares:
    
    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        point_tuple = tuple(point)
        self.points[point_tuple] += 1
    def count(self, point: List[int]) -> int:
        px, py = point
        count_squares = 0
        for (x,y), freq in self.points.items():
            if abs(x - px) == abs(y - py) and x != px and y !=py:
                if (px, y) in self.points and (x,py) in self.points:
                    count_squares += freq*self.points[(px,y)]*self.points[(x,py)]
        return count_squares
        
        
