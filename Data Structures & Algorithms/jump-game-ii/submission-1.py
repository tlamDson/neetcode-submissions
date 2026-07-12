from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0 # jumps = 0,1
        current_end = 0 # current_end = 0,2
        farthest = 0 # farthest = 0,2,5
        # i = 0,1,2
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if farthest == len(nums) - 1:
                return jumps + 1
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps
            

        
            

        
        