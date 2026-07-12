class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        l,r = 0, len(heights) -1 
        maxHeight = 0
        while l <= r:
            current = (r-l)*min(heights[l],heights[r])
            print(current)
            maxHeight = max(maxHeight, current)
            if heights[l] > heights[r]:
                r -=1
            else:
                l += 1

        return maxHeight
       