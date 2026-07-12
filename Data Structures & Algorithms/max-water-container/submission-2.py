class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # greedy 
        # curr_max = max(curr, past_max)
        # glob_max = max(glob_max, curr_max)
        # lấy thanh dài nhất 
        if not heights: return 0
        l, r = 0, len(heights) - 1
        maxHeight = 0
        while l <= r:
            current = (r-l)*min(heights[l], heights[r])
            maxHeight = max(maxHeight, current)
            if heights[l] > heights[r]:
                r -=1
            else:
                l +=1
        return maxHeight
            
        