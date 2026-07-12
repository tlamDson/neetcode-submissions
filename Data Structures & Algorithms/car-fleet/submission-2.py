class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for p,s in cars:
            steps = (target - p) /s
            print(steps)
            if not stack or steps > stack[-1]:
                stack.append(steps)            
        return len(stack)
            
                   