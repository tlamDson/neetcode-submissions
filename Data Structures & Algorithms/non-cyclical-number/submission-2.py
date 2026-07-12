class Solution:
    def isHappy(self, n: int) -> bool:
        line = set()
        while n != 1:
            if n in line: return False
            line.add(n)
            a = 0
            for s in str(n):
                a += int(s) ** 2
            n = a
        return True
        

        