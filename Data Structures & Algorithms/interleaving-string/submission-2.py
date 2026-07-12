from functools import lru_cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        
        @lru_cache(None)
        def dfs(t1,t2):
            #base case
            if t1 + t2 >= len(s3): return True

            match_s1 = t1 < len(s1) and s3[t1 + t2] == s1[t1]
            match_s2 = t2 < len(s2) and s3[t1 + t2] == s2[t2]

            if match_s1 and match_s2:
                return dfs(t1 +1, t2) or dfs(t1,t2 + 1)
            elif match_s1:
                return dfs(t1 + 1, t2)
            elif match_s2: 
                return dfs(t1, t2 + 1)
            else: 
                return False
        return dfs(0,0)


            


        
        