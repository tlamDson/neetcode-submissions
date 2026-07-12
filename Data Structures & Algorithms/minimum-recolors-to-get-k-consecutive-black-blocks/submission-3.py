class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        myDict = {"B": 0, "W": 0}
        l = 0
        res = k # The maximum possible recolors needed is k
        
        for r in range(len(blocks)):
            # 1. Add the current character to the count
            myDict[blocks[r]] += 1 
            
            # 2. If the window is too big, shrink it from the left
            if r - l + 1 > k:
                myDict[blocks[l]] -= 1
                l += 1
            
            # 3. If the window is exactly size k, update the minimum
            if r - l + 1 == k:
                # We want to minimize the number of White blocks to change
                res = min(res, myDict["W"])
                
                # Optimization: If we find a window with 0 whites, we're done
                if res == 0:
                    return 0

        return res