class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        count = 0
        maxS = 0
        char = set()
        while r < len(s):
            while s[r] in char:
                char.remove(s[l])
                count -=1
                l += 1
            char.add(s[r])
            count += 1
            maxS = max(maxS,count)
            r += 1  
        return maxS
            
            


       
        
                