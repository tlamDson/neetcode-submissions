from functools import lru_cache      
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)


        @lru_cache(None)
        def dfs(t1, t2):
            #base case
            if t1 >= n1: 
                return n2 - t2
            if t2 >= n2:
                return n1 - t1
            if word1[t1] != word2[t2]:
                return 1 + min(dfs(t1 + 1, t2),dfs(t1, t2 + 1), dfs(t1 + 1, t2 + 1))
            else: 
                return dfs(t1 + 1, t2 + 1)
        return dfs(0,0)
        
     
        
                

        